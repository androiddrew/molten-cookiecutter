import click
from molten.contrib.sqlalchemy import EngineData
from {{cookiecutter.project_slug}}.index import create_app

app = create_app()


@click.group()
def cli():
    pass


@cli.command()
@click.option("--host", "-h", default="0.0.0.0", help="A hostname or IP address")
@click.option(
    "--port", "-p", default=8000, help="Port number to bind to development server"
)
def runserver(host, port):
    """
    Runs a Werkzueg development server. Do no use for production.
    """
    from werkzeug.serving import run_simple

    run_simple(
        hostname=host, port=port, application=app, use_debugger=True, use_reloader=True
    )


@cli.command()
def shell():
    """
    Enters an interactive shell with an app instance and dependency resolver.
    """
    import rlcompleter
    import readline
    from code import InteractiveConsole

    helpers = {"app": app, "resolver": app.injector.get_resolver()}

    readline.parse_and_bind("tab: complete")
    interpreter = InteractiveConsole(helpers)
    interpreter.interact(f"Instances in scope: {', '.join(helpers)}.", "")


@cli.command()
def initdb():
    """
    Initialize database
    """
    from {{cookiecutter.project_slug}}.db import Base

    def _init(engine_data: EngineData):
        Base.metadata.create_all(bind=engine_data.engine)

    click.echo("Creating database")
    app.injector.get_resolver().resolve(_init)()
    click.echo("Database created")


@cli.command()
def dropdb():
    """
    Drop all tables in database
    """

    from {{cookiecutter.project_slug}}.db import Base

    def _drop(engine_data: EngineData):
        Base.metadata.drop_all(bind=engine_data.engine)

    click.echo("Are you sure you would like to drop the database?: [Y/N]")
    response = input()
    if response.lower() == "y":
        app.injector.get_resolver().resolve(_drop)()
        click.echo("Database dropped")
    else:
        click.echo("Database drop aborted")


if __name__ == "__main__":
    cli()
