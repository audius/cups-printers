# cups-printer

Retrieve all printers from a CUPS server. It's a simple command-line tool that
allows one to output the existing printers or write them to a file.

## Installation

It may require that the development package for CUPS is installed, e.g. 
`$ sudo dnf -y install cups-devel`.

### PyPI

The package is hosted on [PyPI](https://pypi.org/project/cups_printers/).
It depends on `typer` and `pycups`.

```bash
$ pip install cups_printer
```

### Manual setup

```bash
$ python3 -m venv 
$ source bin/activate
$ python3 setup.py
```

## Usage

The default CUPS instance which is used is `localhost`.

```bash
$ cups-printers --help

                                                                                                                           
 Usage: cups-printers [OPTIONS] COMMAND [ARGS]...                                                                          
                                                                                                                           
╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --server                    TEXT  The server URL of CUPS instance [env var: CUPS_SERVER] [default: localhost:631]       │
│ --timeout                   TEXT  Timeout for network operations [env var: TIMEOUT] [default: 5]                        │
│ --install-completion              Install completion for the current shell.                                             │
│ --show-completion                 Show completion for the current shell, to copy it or customize the installation.      │
│ --help                            Show this message and exit.                                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ──────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ output                                                                                                                  │
│ queue                                                                                                                   │
│ state                                                                                                                   │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

To get the details from a remote CUPS instance, use `--server`.

```bash
$ cups-printers --server 192.168.191.1:631 output json
```

## License

`cups-printers` ìs license under MIT.
