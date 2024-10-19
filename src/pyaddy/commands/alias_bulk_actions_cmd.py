"""
Click cmds for the AliasBulkActions
"""

import click
import json
from pyaddy.API import _maybe_raw
from pyaddy.API.alias_bulk_actions import AliasBulkActions


@click.group()
def bulk():
    """Invoke bulk alias commands: --help for details

    addy bulk <subcommand>
    """


@bulk.command(
    name="get-aliases",
    short_help="Get detailed info on aliases. Supply a comma-seperated list of alias IDs -e.g. ID1,ID2. --help for more info",
)
@click.argument("ids")
@click.pass_context
def get_bulk_aliases(ctx, ids):
    """Get detailed info on aliases.

    Supply a comma-seperated list of alias IDs:

    Usage:

    addy [--raw] bulk get-aliases UUID-1,UUID-2,UUID-3
    """

    ids = ids.split(",")
    resp = AliasBulkActions().get_aliases(ids)

    _maybe_raw(ctx, "Detailed Aliases Info:",
               json.dumps(resp.json(), indent=4))


@bulk.command(
    name="activate",
    short_help="Bulk activate list of aliases. Supply a comma-seperated list of alias IDs -e.g. ID1,ID2. --help for more info",
)
@click.argument("ids")
@click.pass_context
def bulk_activate_aliases(ctx, ids):
    """Bulk activate list of aliases

    Supply a comma-seperated list of alias IDs:
    Usage:

    addy [--raw] bulk activate UUID-1,UUID-2,UUID-3
    """

    ids = ids.split(",")
    resp = AliasBulkActions().bulk_activate_aliases(ids)

    _maybe_raw(ctx, "Bulk Activated Aliases Info:",
               json.dumps(resp.json(), indent=4))


@bulk.command(
    name="deactivate",
    short_help="Bulk deactivate list of aliases. Supply a comma-seperated list of alias IDs -e.g. ID1,ID2. --help for more info",
)
@click.argument("ids")
@click.pass_context
def bulk_deactivate_aliases(ctx, ids):
    """Bulk deactivate list of aliases

    Supply a comma-seperated list of alias IDs:

    Usage:

    addy [--raw] bulk deactivate UUID-1,UUID-2,UUID-3
    """

    ids = ids.split(",")
    resp = AliasBulkActions().bulk_deactivate_aliases(ids)

    _maybe_raw(ctx, "Bulk Deactivated Aliases Info:",
               json.dumps(resp.json(), indent=4))


@bulk.command(
    name="delete",
    short_help="Bulk delete list of aliases. Supply a comma-seperated list of alias IDs -e.g. ID1,ID2. --help for more info",
)
@click.argument("ids")
@click.pass_context
def bulk_delete_aliases(ctx, ids):
    """Bulk delete list of aliases

    Supply a comma-seperated list of alias IDs:

    Usage:

    addy [--raw] bulk delete UUID-1,UUID-2,UUID-3
    """

    ids = ids.split(",")
    resp = AliasBulkActions().bulk_deleted_aliases(ids)

    _maybe_raw(ctx, "Bulk Deleted Aliases Info:",
               json.dumps(resp.json(), indent=4))


@bulk.command(
    name="restore",
    short_help="Bulk restore list of aliases. Supply a comma-seperated list of alias IDs -e.g. ID1,ID2. --help for more info",
)
@click.argument("ids")
@click.pass_context
def bulk_restore_aliases(ctx, ids):
    """Bulk restore list of aliases

    Supply a comma-seperated list of alias IDs:\n
    Usage:\n

    addy bulk restore UUID-1,UUID-2,UUID-3
    """

    ids = ids.split(",")
    resp = AliasBulkActions().bulk_restore_aliases(ids)

    _maybe_raw(ctx, "Bulk Restore Aliases Info:",
               json.dumps(resp.json(), indent=4))
