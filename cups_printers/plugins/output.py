"""Output plugin for the CUPS printers CLI."""
import json as _json
import sys

import click

from cups_printers.cli import pass_context


@click.group('output')
@pass_context
def cli(ctx):
    """Output the retrieved data from a CUPS instance."""


@cli.command()
@pass_context
def raw(ctx):
    """Display the raw data."""
    printers = ctx.conn.getPrinters()

    for printer in printers:
        details = printers[printer]
        click.echo("%s, %s" % (printer, details))


@cli.command()
@pass_context
def json(ctx):
    """Output as JSON formatted string."""
    output = get_printer(ctx)
    click.echo(_json.dump(
        output, sys.stdout, sort_keys=True, indent=2, ensure_ascii=False))


@cli.command()
@pass_context
def file(ctx):
    """Write output to file as JSON formatted string."""
    output = get_printer(ctx)

    with open('printers.json', 'w') as outfile:
        _json.dump(
            output, outfile, sort_keys=True, indent=2, ensure_ascii=False)

    click.echo("Content of printers.conf updated")


def get_printer(ctx):
    """Get all printers."""
    output = {}
    list_printers = []

    printers = ctx.conn.getPrinters()

    for printer in printers:
        attrs = ctx.conn.getPrinterAttributes(printer)
        list_printers.append(attrs)

    output['printers'] = list_printers

    return output
