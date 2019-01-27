# {{ cookiecutter.project_name }}

{{cookiecutter.description}}

## First time setup

Create a virtual environment and activate it. Now from the root project directory run `./scripts/bootstrap`. This will install `pip-tools` and sync any dependencies for the first time.

To run the app you will need a [postgres] database. Create a development and a test database. Update the connection strings within the `{{cookiecutter.project_slug}}.settings.toml`. At this time, if you choose to, you can remove the demo `Todo` code and replace it with your own Model. Otherwise create your first [alembic] migration using the `alembic revision --autogenerate -m "your revision message"` command. Finally, apply your first migration with `alembic upgrade head`. 


## Running the developement server
A `manage.py` script has been included with a collection of [click] cli functions to assist in development.
 
__Note__: the developement server command is not a production webserver. You will need to c

```
python manage.py runserver
```

## Using the interactive interpreter
The `manage.py` script can be used to open an interactive interpreter with a configured molten application from your project.
```
python manage.py shell
```

## Dependency management

Dependencies are managed via [pip-tools].

### Adding a dependency

To add a dependency, edit `requirements.in` (or `dev_requirements.in`
for dev dependencies) and add your dependency then run `pip-compile
requirements.in`.

### Syncing dependencies

Run `pip-sync requirements.txt dev_requirements.txt`.


## Migrations

Migrations are managed using [alembic].

### Generating new migrations

    alembic revision --autogenerate -m 'message'

### Running the migrations

    alembic upgrade head  # to upgrade the local db
    env ENVIRONMENT=test alembic upgrade head  # to upgrade the test db
    env ENVIRONMENT=prod alembic upgrade head  # to upgrade prod
    
## Testing

Run the tests by invoking `py.test` in the project root.  Make sure you
run any pending migrations beforehand.

[alembic]: http://alembic.zzzcomputing.com/en/latest/
[click]: https://click.palletsprojects.com
[pip-tools]: https://github.com/jazzband/pip-tools
[postgres]: https://www.postgresql.org/