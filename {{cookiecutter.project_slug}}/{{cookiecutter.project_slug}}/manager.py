from abc import ABCMeta, abstractmethod
from molten import BaseApp, HTTPError, HTTP_409, HTTP_404
from sqlalchemy.orm import Session


class BaseManager(metaclass=ABCMeta):
    """Base instance for Model managers"""

    def __init__(self, session: Session, app: BaseApp):
        self.session = session
        self.app = app

    @abstractmethod
    def model_from_schema(self, schema):
        """Converts a Schema instance into a SQLAlchemy ORM model instance"""
        pass

    @abstractmethod
    def schema_from_model(self, result):
        """Converts a SQLAlchemy results proxy into a Schema instance"""
        pass

    def raise_409(self, id:int):
        """Raises a 409 HTTP error response in the event of Conflict"""
        raise HTTPError(
            HTTP_409,
            {
                "status": 409,
                "message": f"Entity {self.__class__.__name__} with id: {id} already exists"
            }

        )
