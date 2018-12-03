"""CUPS printers CLI."""
import os

import click

import cups
from cups_printers.config import Configuration
from cups_printers.const import (
    DEFAULT_SERVER, DEFAULT_TIMEOUT, PACKAGE_NAME, __version__)

CONTEXT_SETTINGS = dict(auto_envvar_prefix='CUPSPRINTERS')

pass_context = click.make_pass_decorator(Configuration, ensure=True)
cmd_folder = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 'plugins'))


class CupsPrintersCli(click.MultiCommand):
    """The CUPS printers command-line interface."""

    def list_commands(self, ctx):
        """List all command available as plugin."""
        commands = []
        for filename in os.listdir(cmd_folder):
            if filename.endswith('.py') and not filename.startswith('__'):
                commands.append(filename[:-3])
        commands.sort()

        return commands

    def get_command(self, ctx, name):
        """Import the commands of the plugins."""
        try:
            mod = __import__(
                '{}.plugins.{}'.format(PACKAGE_NAME, name), None, None, ['cli'])
        except ImportError:
            return
        return mod.cli


@click.command(cls=CupsPrintersCli, context_settings=CONTEXT_SETTINGS)
@click.version_option(__version__)
@click.option('--server', '-s',
              help='The server URL of CUPS instance.',
              default=DEFAULT_SERVER, show_default=True, envvar='CUPS_SERVER')
@click.option('--timeout',
              help='Timeout for network operations.', default=DEFAULT_TIMEOUT)
@pass_context
def cli(ctx, server, timeout,):
    """A command line interface for CUPS printers."""

    ctx.server = server
    ctx.timeout = timeout

    try:
        cups.setServer(server)
        ctx.conn = cups.Connection()
    except RuntimeError:
        click.echo("Server not available or unable to connect")
        raise SystemExit
