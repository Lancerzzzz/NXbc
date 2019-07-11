from nxapi.cli_base.cli_base import cli_base
import json


def query_route_all(serial):
    cli = "show ip route vrf all"
    query = cli_base(serial, cli)
    response = json.loads(query.send().text)
    data = response['ins_api']['outputs']['output']['body']['TABLE_vrf']['ROW_vrf']
    return data


# name = default
def query_route_vrf(serial, name):
    cli = "show ip route vrf " + name
    query = cli_base(serial, cli)
    response = json.loads(query.send().text)
    data = response['ins_api']['outputs']['output']['body']['TABLE_vrf']['ROW_vrf']['TABLE_addrf']['ROW_addrf'][
        'TABLE_prefix']['ROW_prefix']
    return data
