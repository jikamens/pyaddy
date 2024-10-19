"""
Click cmds for the AddyApiDetails class
"""


import click
import json
from pyaddy.API import _maybe_raw
from pyaddy.API.api_details import AddyApiDetails


@click.group()
def api():
    """Invoke details about the provided api key"""


@api.command(name="api-details")
@click.pass_context
def check_api_key_details(ctx):
    """Check the details of the api key"""
    resp = AddyApiDetails().get_api_details()

    _maybe_raw(ctx, "API details:", json.dumps(resp.json(), indent=4))


@api.command(name="account-details")
@click.pass_context
def get_account_details(ctx):
    """Get all account details associated with api key"""
    resp = AddyApiDetails().get_account_details()

    _maybe_raw(ctx, "Account Details:", json.dumps(resp.json(), indent=4))
