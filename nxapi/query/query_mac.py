from nxapi.cli_base.cli_base import cli_base
import json


# show int e1/112 mac
def query_onemac(serial, eth):
    cli = "show int " + eth + " mac"
    query = cli_base(serial, cli)
    response = json.loads(query.send().text)
    onemac = response['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']
    return onemac


# show int mac
def query_allmac(serial):
    cli = "show int mac"
    query = cli_base(serial, cli)
    response = json.loads(query.send().text)
    onemac = response['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']
    return onemac
