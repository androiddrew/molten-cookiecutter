from typing import Tuple
from molten import App, Route, ResponseRendererMiddleware
from molten.http import HTTP_404, Request
from molten.settings import Settings, SettingsComponent
from molten.contrib.sqlalchemy import SQLAlchemyMiddleware

from .api.welcome import welcome
from .common import ExtJSONRenderer
from .schema import APIResponse

settings = Settings({})

components = [
    SettingsComponent(settings),
]

middleware = [ResponseRendererMiddleware(), SQLAlchemyMiddleware()]

renderers = [ExtJSONRenderer()]

routes = [Route("/", welcome, "GET")]


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


def create_app(_components=None, _middleware=None, _routes=None, _renderers=None):
    """
    Factory function for the creation of a `molten.App` instance
    """
    app = ExtApp(
        components=_components or components,
        middleware=_middleware or middleware,
        routes=_routes or routes,
        renderers=_renderers or renderers
    )
    return app
