import click


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
    from {{cookiecutter.project_slug}}.index import create_app
    from werkzeug.serving import run_simple

    app = create_app()

    run_simple(
        hostname=host, port=port, application=app, use_debugger=True, use_reloader=True
    )


@cli.command()
def shell():
    """
    Enters an interactive shell with an app instance and dependency resolver.
    """
    import readline
    from code import InteractiveConsole

    from {{cookiecutter.project_slug}}.index import create_app

    app = create_app()

    helpers = {"app": app, "resolver": app.injector.get_resolver()}

    readline.parse_and_bind("Tab: complete")
    interpreter = InteractiveConsole(helpers)
    interpreter.interact(
        f"""\
    Instances in scope: {", ".join(helpers)}.
    """,
        "",
    )


@cli.command()
def initdb():
    """
    Initialize database
    """
    from {{cookiecutter.project_slug}}.db import Base

    click.echo("Creating database")
    Base.metadata.create_all(bind=engine)
    click.echo("Database created")


@cli.command()
def dropdb():
    """
    Drop all tables in database
    """

    from {{cookiecutter.project_slug}}.db import Base

    click.echo("Are you sure you would like to drop the database?: [Y/N]")
    response = input()
    if response.lower() == "y":
        Base.metadata.drop_all(bind=engine)
        click.echo("Database dropped")
    else:
        click.echo("Database drop aborted")


if __name__ == "__main__":
    cli()
