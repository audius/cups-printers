"""Queue plugin for the CUPS printers CLI."""

import typer

from rich.console import Console
from rich.table import Table

app = typer.Typer()


@app.command()
def query(ctx: typer.Context):
    """Display the queue."""
    connection = ctx.obj.get("connection")

    jobs = connection.getJobs(
        which_jobs="all",
        requested_attributes=["job-id", "job-name", "job-state", "job-printer-name"],
    )

    table = Table(title="Queue")

    table.add_column("Job", justify="left", style="cyan", no_wrap=True)
    table.add_column("State")

    for job, state in jobs.items():
        table.add_row(str(job), str(state["job-state"]))

    console = Console()
    console.print(table)
