"""Queue plugin for the CUPS printers CLI."""

import typer

app = typer.Typer()


@app.command()
def query(ctx: typer.Context):
    """Display the queues."""
    connection = ctx.obj.get("connection")

    typer.echo(f"Not implemented, sorry.")
