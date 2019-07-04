from nxapi.cli_base.cli_base import cli_base
import json


def query_route(serial):
    cli = "show ip route"
    query = cli_base(serial, cli)
    response = json.loads(query.send().text)
    data = response['ins_api']['outputs']['output']['body']['TABLE_vrf']['ROW_vrf']['TABLE_addrf']['ROW_addrf']
    return data
