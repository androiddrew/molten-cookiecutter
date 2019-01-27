from typing import Tuple
from molten import App, Route, ResponseRendererMiddleware, Settings
from molten.http import HTTP_404, Request
from molten.openapi import Metadata, OpenAPIHandler, OpenAPIUIHandler
from molten.settings import SettingsComponent
from molten.contrib.sqlalchemy import SQLAlchemyMiddleware, SQLAlchemyEngineComponent, SQLAlchemySessionComponent
{%- if cookiecutter.cors_support == 'y' %}
from wsgicors import CORS
{%- endif %}
{%- if cookiecutter.static_support == 'y' %}
from whitenoise import WhiteNoise
{%- endif %}

from .api.welcome import welcome
from .api.todo import TodoManagerComponent, todo_routes
from .common import ExtJSONRenderer
from .logging import setup_logging
from .schema import APIResponse
from . import settings

get_schema = OpenAPIHandler(
    metadata=Metadata(
        title="{{cookiecutter.project_slug}}",
        description="{{cookiecutter.description}}",
        version="0.0.0"
    )
)

get_docs = OpenAPIUIHandler()

components = [
    SettingsComponent(settings),
    SQLAlchemyEngineComponent(),
    SQLAlchemySessionComponent(),
    TodoManagerComponent(),
]

middleware = [ResponseRendererMiddleware(), SQLAlchemyMiddleware()]

renderers = [ExtJSONRenderer()]

routes = [
             Route("/", welcome, "GET"),
             Route("/_schema", get_schema, "GET"),
             Route("/_docs", get_docs, "GET"),
         ] + [todo_routes]


class ExtApp(App):
    def handle_404(self, request: Request) -> Tuple[str, APIResponse]:
        """
        Returns as standardized JSONResponse on HTTP 404 Error.
        """
        return (
            HTTP_404,
            APIResponse(
                status=404,
                message=f"The resource you are looking for {request.scheme}://{request.host}{request.path} doesn't exist",
            ),
        )

    @property
    def settings(self):
        def _get_settings(_settings: Settings):
            return _settings

        settings = self.injector.get_resolver().resolve(_get_settings)()
        return settings


def create_app(_components=None, _middleware=None, _routes=None, _renderers=None):
    """
    Factory function for the creation of a `molten.App`.
    """
    setup_logging()

    wrapped_app = app = ExtApp(
        components=_components or components,
        middleware=_middleware or middleware,
        routes=_routes or routes,
        renderers=_renderers or renderers
    )

    {%- if cookiecutter.cors_support == 'y' %}
    wrapped_app = CORS(wrapped_app,  **settings.strict_get("wsgicors"))
    {%- endif %}

    {%- if cookiecutter.static_support == 'y' %}
    wrapped_app = WhiteNoise(wrapped_app, **settings.strict_get("whitenoise"))
    {%- endif %}

    return wrapped_app, app
