"""
Click cmds for the Aliases class
"""

import click
import json
from pyaddy.API import _maybe_raw
from pyaddy.API.aliases import Aliases


@click.group()
def alias():
    """Invoke alias commands: --help for details

    addy alias <subcommand>"""


@alias.command(
    name="get-all",
    short_help="Get details about all ACTIVE aliases SORTED by CREATED_AT. OPTION: --only-ids",
)
@click.option("--only-ids", help="only show IDs", is_flag=True)
@click.pass_context
def get_all_aliases(ctx, only_ids):
    """Get all aliases

    Default: Get all ACTIVE aliases SORTED by CREATED_AT:

    Usage:

    addy [--raw] alias get-all
    addy [--raw] alias get-all --only-ids
    """

    # TODO: look into filter options
    params = {
        "filter[active]": "true",
        "sort": "-created_at",
    }

    resp = Aliases().get_aliases_page(params)
    resp_json = resp.json()
    data = resp_json["data"]
    while resp_json["meta"]["current_page"] < resp_json["meta"]["last_page"]:
        resp = Aliases().get_aliases_page(
            params, page=resp_json["meta"]["current_page"]+1)
        resp_json = resp.json()
        data += resp_json["data"]

    if only_ids:
        _maybe_raw(ctx, "Alias IDs:",
                   (",".join(aliases["id"] for aliases in data)))
    else:
        _maybe_raw(ctx, "All Aliases:", json.dumps(data, indent=4))


@alias.command("get", short_help="Get ID details")
@click.argument("id")
@click.pass_context
def get_specific_alias(ctx, id):
    """Get ID details

    Usage:

    addy [--raw] alias get UUID
    """

    resp = Aliases().get_specific_alias(id)
    _maybe_raw(ctx, "Alias Info:", json.dumps(resp.json(), indent=4))


@alias.command(name="new", short_help="Create a new alias. --help for all options")
@click.option(
    "--domain",
    help="the domain of the alias. Default addymail.com",
    default="addymail.com",
    type=str,
)
@click.option(
    "--description",
    help='the description of the alias. NOTE: put description in quotes "Description Foo Bar" ',
    type=str,
)
@click.option(
    "--format",
    help="chosen format for the alias: random_characters, uuid, or random_words",
    type=str,
)
@click.option(
    "--recipient-id",
    help="recipient id to add. Default recipient will be used if non is provided",
    type=str,
)
@click.pass_context
def create_new_alias(ctx, domain, description, format, recipient_id):
    """Create a new alias

    Usage:

    addy [--raw] alias new
    addy [--raw] alias new --domain addymail.com --description "addy created" --format random_words
    """

    payload = {
        "domain": domain,
        "description": description,
        "format": format,
        "recipient_id": recipient_id,
    }

    resp = Aliases().create_new_alias(payload)
    _maybe_raw(ctx, "Create New Alias Info:",
               json.dumps(resp.json(), indent=4))


@alias.command(name="update", short_help='Update alias "descprition" and "from_name"')
@click.argument("id")
@click.option(
    "--description",
    help='Updated DESCRIPTION: NOTE: put string in quotes: "PyAddy Update" Default: PyAddy Update',
    default="PyAddy Update",
)
@click.option(
    "--from-name",
    help='Updated FROM_NAME: NOTE: put string in quotes "Leonardo T." Default: Leonardo T.',
    default="Lenoardo T.",
)
@click.pass_context
def update_specific_alias(ctx, id, description, from_name):
    """Update alias "descprition" and "from_name"

    Usage:

    addy [--raw] alias update UUID --description "foo addy" --from-name "bar addy"
    """

    payload = {"description": description, "from_me": from_name}

    resp = Aliases().update_specific_alias(id, payload)
    _maybe_raw(ctx, f"Updated {id} Info:",
               json.dumps(resp.json(), indent=4))


@alias.command(name="restore", short_help="Restore alias ID")
@click.argument("id")
@click.pass_context
def restore_deleted_alias(ctx, id):
    """Restore an alias ID

    Usage:

    addy [--raw] alias restore UUID
    """

    resp = Aliases().restore_specific_alias(id)
    _maybe_raw(ctx, f"Restored {id} Info:",
               json.dumps(resp.json(), indent=4))


@alias.command(name="delete", short_help="Delete alias ID")
@click.argument("id")
def delete_specific_alias(id):
    """Delete an alias ID

    Usage:

    addy alias delete UUID
    """

    Aliases().delete_specific_alias(id)
    click.echo(f"Deleted {id}")


@alias.command(name="forget", short_help="Forget alias ID")
@click.argument("id")
def forget_specific_alias(id):
    """Forget an alias ID

    Usage:\n
    addy alias forget UUID
    """

    Aliases().forget_specific_alias(id)
    click.echo(f"Forgot {id}")


@alias.command(name="activate", short_help="Activate alias ID")
@click.argument("id")
@click.pass_context
def activate_alias(ctx, id):
    """Activate an alias ID

    Usage:

    addy [--raw] alias activate UUID
    """

    payload = {"id": id}
    resp = Aliases().activate_alias(payload)
    _maybe_raw(ctx, f"Activated {id} Info:",
               json.dumps(resp.json(), indent=4))


@alias.command(name="deactivate", short_help="Deactivate alias ID")
@click.argument("id")
def deactivate_alias(id):
    """Deactivate alias ID

    Usage:\n
    addy alias deactivate UUID
    """

    Aliases().deactivate_alias(id)
    click.echo(f"Deactivated {id}")
