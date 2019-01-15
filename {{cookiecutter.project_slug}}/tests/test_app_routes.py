def test_welcome_route(client):
    message = "welcome to {{cookiecutter.project_slug}}"
    response = client.get("/")
    content = response.json()
    assert message == content.get("message")


def test_empty_get_todos(client):
    response = client.get("/todos")
    assert response.status_code == 200
    assert response.json() == []


def test_insert_todo(client):
    payload = {"todo": "walk the dog"}
    response = client.post("/todos", data=payload)
    content = response.json()
    assert response.status_code == 201
    assert type(content['id']) == int
    assert content['todo'] == payload['todo']


def test_get_individual_todo_by_href(client):
    payload = {"todo": "my individual todo"}
    response = client.post("/todos", data=payload)
    content = response.json()
    get_response = client.get(f"{content.get('href')}")
    get_content = get_response.json()
    assert get_response.status_code == 200
    assert content == get_content


def test_update_todo(client):
    payload = {"todo": "sample app"}
    response = client.post("/todos", json=payload)
    todo = response.json()
    update_response = client.patch("{}".format(todo.get("href")), json={"complete": True, "todo": "sample app"})
    updated_todo = update_response.json()
    assert updated_todo["complete"] == True


def test_todo_not_found(client):
    response = client.get("/todo/1111111")
    content = response.json()
    assert response.status_code == 404
    assert content["status"] == 404
    assert content["message"]


def test_delete_todo(client):
    payload = {"todo": "sample app"}
    response = client.post("/todos", json=payload)
    todo = response.json()
    delete_response = client.delete(f"/todos/{todo.get('id')}")
    assert delete_response.status_code == 202
