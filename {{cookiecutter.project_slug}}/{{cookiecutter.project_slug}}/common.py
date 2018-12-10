import datetime as dt
from os import path
from decimal import Decimal
from typing import Any
from molten import JSONRenderer, is_schema, dump_schema

BASE_PATH = path.normpath(path.join(path.abspath(path.dirname(__file__)), "."))


def path_to(*xs):
    """
    Construct a path from the root project directory
    """
    return path.join(BASE_PATH, *xs)


class ExtJSONRenderer(JSONRenderer):
    """JSON Render with support for ISO 8601 datetime format strings and Decimal"""

    def default(self, ob: Any) -> Any:
        """You may override this when subclassing the JSON renderer in
        order to encode non-standard object types.
        """
        if is_schema(type(ob)):
            return dump_schema(ob)
        if isinstance(ob, dt.datetime):
            return ob.isoformat()
        if isinstance(ob, Decimal):
            return float(ob)

        raise TypeError(f"cannot encode values of type {type(ob)}")  # pragma: no cover
