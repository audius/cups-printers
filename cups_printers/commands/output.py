"""Output plugin for the CUPS printers CLI."""
import json as _json
import sys

import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer()


def get_printer(ctx: typer.Context):
    """Get all printers."""
    connection = ctx.obj.get("connection")

    output = {}
    list_printers = []

    printers = connection.getPrinters()

    for printer in printers:
        attrs = connection.getPrinterAttributes(printer)
        list_printers.append(attrs)

    output["printers"] = list_printers

    return output


@app.command()
def raw(ctx: typer.Context):
    """Display the raw data."""
    connection = ctx.obj.get("connection")

    printers = connection.getPrinters()

    for printer in printers:
        details = printers[printer]
        typer.echo(f"{printer}: {details}")


@app.command()
def table(ctx: typer.Context):
    """Display the data as table."""
    connection = ctx.obj.get("connection")

    printers = connection.getPrinters()

    for printer in printers:
        details = printers[printer]
        typer.echo(f"{printer}: {details}")

    table = Table(title="Printer details")

    table.add_column("Printer", justify="left", style="cyan", no_wrap=True)
    table.add_column("Model")
    table.add_column("Info")
    table.add_column("Location")
    table.add_column("Shared?")
    table.add_column("State")
    table.add_column("State message")
    table.add_column("State reason")
    table.add_column("Type")
    table.add_column("URI")
    table.add_column("Device URI")

    for printer in printers:
        details = printers[printer]
        table.add_row(
            printer,
            details["printer-make-and-model"],
            details["printer-location"],
            details["printer-info"],
            str(bool(details["printer-is-shared"])),
            str(details["printer-state"]),
            str(details["printer-state-message"]),
            str(details["printer-state-reasons"][0]),
            str(details["printer-type"]),
            details["printer-uri-supported"],
            details["device-uri"],
        )

    console = Console()
    console.print(table)


@app.command()
def json(ctx: typer.Context):
    """Output as JSON formatted string."""
    output = get_printer(ctx)
    print(output)
    print(_json.dump(output, sys.stdout, sort_keys=True, indent=2, ensure_ascii=False))


@app.command()
def file(ctx: typer.Context):
    """Write output to file as JSON formatted string."""
    output = get_printer(ctx)

    with open("printers.json", "w") as outfile:
        _json.dump(output, outfile, sort_keys=True, indent=2, ensure_ascii=False)

    typer.echo("Content of printers.conf written to disk")
