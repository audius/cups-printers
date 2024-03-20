"""State plugin for the CUPS printers CLI."""
import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer()


@app.command()
def raw(ctx: typer.Context):
    """Display the current state of all printers in a greppable format."""
    connection = ctx.obj.get("connection")

    printers = connection.getPrinters()

    for printer in printers:
        typer.echo(
            f"{printers[printer]['printer-info']}, {printers[printer]['printer-state']}"
        )


@app.command()
def table(ctx: typer.Context):
    """Display current state of all printers as table."""
    connection = ctx.obj.get("connection")

    printers = connection.getPrinters()

    table = Table(title="Printer states")

    table.add_column("Printer", justify="left", style="cyan", no_wrap=True)
    table.add_column("State")

    for printer in printers:
        details = printers[printer]
        table.add_row(
            printer,
            str(details["printer-state"]),
        )

    console = Console()
    console.print(table)
