import click

from dev_util.dev import dev_group


@dev_group("db")
@click.pass_context
def db(ctx: click.Context) -> None:
    pass
