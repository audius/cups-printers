# cups_printer

Retrieve all printer from a CUPS server. It's a simple command-line tool that
allows one to output the existing printers or write them to a file.

## Installation

It may require that the development package for CUPS is installed, e.g. 
`$ sudo dnf -y install cups-devel`.

### PyPI

The package is hosted on [PyPI](https://pypi.org/project/cups_printers/).
It depends on `click` and `pycups`.

```bash
$ pip3 install cups_printer
```

### Manual setup

```bash
$ python3 -m venv 
$ source bin/activate
$ python3 setup.py
```

### Development setup

For development, clone the Git repository and create a Python virtual 
environment.

```bash
$ python3 -m venv 
$ source bin/activate
$ python3 setup.py develop
```

## Usage

The default CUPS instance which is used is `localhost`.

```bash
$ cups_printers --help
Usage: cups_printers [OPTIONS] COMMAND [ARGS]...

  A command line interface for CUPS printers.

Options:
  --version          Show the version and exit.
  -s, --server TEXT  The server URL of CUPS instance.  [default:
                     localhost:631]
  --timeout INTEGER  Timeout for network operations.
  --help             Show this message and exit.

Commands:
  output  Output the retrieved data from a CUPS instance.
  state   Print the current state of all printers.
```

To get the details from a remote CUPS instance, use `--server`.

```bash
$ cups_printers --server 192.168.191.1:631 output json
```

## License

`cups_printers` ìs license under MIT.