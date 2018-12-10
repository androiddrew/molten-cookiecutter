from inspect import Parameter
from typing import List
from molten import BaseApp, HTTPError, HTTP_409, HTTP_404
from sqlalchemy.orm import Session

from {{cookiecutter.project_slug}}.manager import BaseManager
from {{cookiecutter.project_slug}}.error import EntityNotFound
from .model import Todo, TodoModel


class TodoManager(BaseManager):
    """A `TodoManager` is  accountable for the CRUD operations associated with a `Todo` instance"""

    def schema_from_model(self, result: TodoModel) -> Todo:
        _todo = Todo(
            id=result.id,
            href=self.app.reverse_uri("get_todo_by_id", todo_id=result.id),
            createdDate=result.created_date,
            modifiedDate=result.modified_date,
            todo=result.todo,
            complete=result.complete
        )
        return _todo

    def model_from_schema(self, todo: Todo) -> TodoModel:
        _todo_model = TodoModel(
            todo=todo.todo,
            complete=todo.complete
        )
        return _todo_model

    def get_todos(self) -> List[Todo]:
        """Retrieves a list of `Todo` representations"""
        results = self.session.query(TodoModel).order_by(TodoModel.id).all()
        todos = [self.schema_from_model(result) for result in results]
        return todos

    def get_todo_by_id(self, id) -> Todo:
        """Retrieves a `Todo` representation by id"""
        result = self.session.query(TodoModel).filter_by(id=id).one_or_none()
        if result is None:
            raise EntityNotFound(f"Todo: {id} does not exist")
        return self.schema_from_model(result)

    def create_todo(self, todo: Todo) -> Todo:
        """Creates a new `Todo` resource and returns its representation"""
        todo_model = self.model_from_schema(todo)
        self.session.add(todo_model)
        self.session.flush()
        return self.schema_from_model(todo_model)

    def update_todo(self, todo_id: int, todo: Todo) -> Todo:
        """Updates an existing `Todo` resource and returns its new representation"""
        result = self.session.query(TodoModel).filter_by(id=todo_id).one_or_none()
        if result is None:
            raise EntityNotFound(f"Todo: {todo_id} does not exist")
        updates = self.model_from_schema(todo)
        updates.id = todo_id
        self.session.merge(updates)
        self.session.flush()
        todo = self.schema_from_model(result)
        return todo

    def delete_todo(self, id):
        """Deletes a `Todo` """
        result = self.session.query(TodoModel).filter_by(id=id).one_or_none()
        if result is not None:
            self.session.delete(result)
        return


class TodoManagerComponent:
    is_cacheable = True
    is_singleton = False

    def can_handle_parameter(self, parameter: Parameter) -> bool:
        return parameter.annotation is TodoManager

    def resolve(self, session: Session, app: BaseApp) -> TodoManager:  # type: ignore
        return TodoManager(session, app)
