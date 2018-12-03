"""Configuration for CUPS printers."""
from cups_printers.const import DEFAULT_SERVER


class Configuration(object):
    """The configuration context for the CUPS printer CLI."""

    def __init__(self):
        """Initialize the configuration."""

        self.verbose = False
        self.server = DEFAULT_SERVER
