"""
Click cmds for the Domain class
"""

import click
import json
from pyaddy.API import _maybe_raw
from pyaddy.API.domain import Domain

@click.group()
def domain():
    """Invoke domain commands: --help for details

    addy domain <subcommand>
    """

@domain.command(name="all-options",
                short_help="retrieves all domain options")
@click.pass_context
def get_all_domain_options(ctx):
    """Retrieve all domain options"""

    resp = Domain().get_all_domain_options()
    _maybe_raw(ctx, "All Domain Options:",
               json.dumps(resp.json(), indent=4))


@domain.command(name="all",
                short_help="retrieves all domains")
@click.pass_context
def get_all_domains(ctx):
    """Retrieve all domains"""

    resp = Domain().get_all_domains()
    _maybe_raw(ctx, "All Domains:", json.dumps(resp.json(), indent=4))

@domain.command(name="get",
                short_help="get details of a specific domain ID")
@click.argument("id")
@click.pass_context
def get_specific_domain(ctx, id):
    """Get the details of a specific domain id
    
    Usage:

    addy [--raw] domain get 0ad7a75a-1517-4b86-bb8a-9443d4965e60
    """

    resp = Domain().get_specific_domain(id)
    _maybe_raw(ctx, "All Domains:", json.dumps(resp.json(), indent=4))


@domain.command(name="create-new",
                short_help="create a new domain with the given NAME")
@click.argument("name")
@click.pass_context
def create_new_domain(ctx, name: str):
    """Create a new domain with the given NAME

    Usage:

    addy [--raw] domain create-new example.com
    """

    payload = {"domain": name}
    resp = Domain().create_new_domain(payload)
    _maybe_raw(ctx, "Created Domain:", json.dumps(resp.json(), indent=4))
