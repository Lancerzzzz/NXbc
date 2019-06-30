from nxapi.cli_base.cli_base import cli_base
import json


def query_interface_all(serial):
    cli = "show interface brief"
    query = cli_base(serial, cli)
    response = json.loads(query.send().text)
    data = response['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']
    return data

