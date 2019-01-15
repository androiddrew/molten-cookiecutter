from typing import List
from molten import Route, Include, HTTP_201, HTTP_202, HTTPError, HTTP_404

from {{cookiecutter.project_slug}}.schema import APIResponse
from {{cookiecutter.project_slug}}.error import EntityNotFound
from .model import Todo
from .manager import TodoManager


def list_todos(todo_manager: TodoManager) -> List[Todo]:
    return todo_manager.get_todos()


def create_todo(todo: Todo, todo_manager: TodoManager) -> Todo:
    _todo = todo_manager.create_todo(todo)
    headers = {"Location": _todo.href}
    return HTTP_201, _todo, headers


def delete_todo(todo_id: int, todo_manager: TodoManager):
    todo_manager.delete_todo(todo_id)
    return (
        HTTP_202,
        APIResponse(status=202, message=f"Delete request for todo: {todo_id} accepted"),
    )


def get_todo_by_id(todo_id: int, todo_manager: TodoManager) -> Todo:
    try:
        _todo = todo_manager.get_todo_by_id(todo_id)
    except EntityNotFound as err:
        raise HTTPError(HTTP_404,
                        APIResponse(status=404,
                                    message=err.message)
                        )
    return _todo


def update_todo(todo_id: int, todo: Todo, todo_manager: TodoManager) -> Todo:
    return todo_manager.update_todo(todo_id, todo)


todo_routes = Include("/todos", [
    Route("", list_todos, method="GET"),
    Route("", create_todo, method="POST"),
    Route("/{todo_id}", delete_todo, method="DELETE"),
    Route("/{todo_id}", get_todo_by_id, method="GET"),
    Route("/{todo_id}", update_todo, method="PATCH")
])
