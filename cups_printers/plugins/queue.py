"""Queue plugin for the CUPS printers CLI."""
import click

from cups_printers.cli import pass_context


@click.command('queue')
@pass_context
def cli(ctx):
    """Print the current queue content of all printers."""

    click.echo("Lalalala....not implemented")
