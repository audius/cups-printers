"""State plugin for the CUPS printers CLI."""
import typer

app = typer.Typer()


@app.command()
def raw(ctx: typer.Context):
    """Display the current state of all printers in a greppable format."""
    connection = ctx.obj.get("connection")

    printers = connection.getPrinters()

    for printer in printers:
        typer.echo(f"{printers[printer]['printer-info']}, {printers[printer]['printer-state']}")
