import click

def _maybe_raw(ctx, title, body):
    if not ctx.parent.parent.params["raw"]:
        click.echo(title)
    click.echo(body)
