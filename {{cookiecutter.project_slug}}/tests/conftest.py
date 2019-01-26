import pytest

from molten import testing
from molten.contrib.sqlalchemy import EngineData

from {{cookiecutter.project_slug}}.index import create_app
from {{cookiecutter.project_slug}}.db import Base



# requires function scope so that database is removed on every tests
@pytest.fixture(scope="function")
def app():
    _, app = create_app()
    yield app


@pytest.fixture(autouse=True)
def create_db(app):
    """Creates a test database with session scope"""
    def _retrieve_engine(engine_data: EngineData):
        return engine_data.engine

    engine = app.injector.get_resolver().resolve(_retrieve_engine)()

    Base.metadata.create_all(bind=engine)

    yield

    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(app):
    """Creates a testing client"""
    return testing.TestClient(app)



@pytest.fixture(scope="function")
def session():
    pass