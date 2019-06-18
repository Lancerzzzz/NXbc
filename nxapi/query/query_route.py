from nxapi.cli_base.cli_base import cli_base
import json

# name = all, manager, default
# 使用：query_route(serial, name), query_route(serial)
# name default all
def query_route(serial, *name):
    if len(name) == 0:
        cli = "show ip route vrf all"
    else:
        cli = "show ip route vrf " + name[0]
    query = cli_base(serial, cli)
    response = json.loads(query.send().text)
    data = response['ins_api']['outputs']['output']['body']['TABLE_vrf']['ROW_vrf']
    return data
