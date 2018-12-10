from molten.testing import TestClient
from {{cookiecutter.project_slug}}.index import create_app

app = create_app()
test_client = TestClient(app)


def test_welcome_route():
    message = "welcome to {{cookiecutter.project_slug}}"
    response = test_client.get("/")
    content = response.json()
    assert message == content.get("message")
