from nxapi.cli_base.cli_base import cli_base
import json

# eth = eth1/5
# query_mac(serial)
# query_mac(serial, eth)
def query_onemac(serial, *eth):
    if len(eth) == 0:
        cli = "show int mac"
    else:
        cli = "show int " + eth + " mac"
    query = cli_base(serial, cli)
    response = json.loads(query.send().text)
    onemac = response['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']
    return onemac
