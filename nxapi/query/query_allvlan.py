from nxapi.cli_base.cli_base import cli_base
import json



def query_vlan(serial):
    cli ="show vlan b"
    a = cli_base(serial,cli)
    response = json.loads(a.send().text)
    vlanbri = response['ins_api']['outputs']['output']['body']['TABLE_vlanbriefxbrief']['ROW_vlanbriefxbrief']
    return vlanbri

def query_onevlan(serial,eth)
    cli="show vlan id"+eth
    b = cli_base(serial,cli)
    response = json.loads(b.send().text)
    onevlan = response['ins_api']['outputs']['output']['body']['TABLE_vlanbriefxbrief']['ROW_vlanbriefxbrief']
    return onevlan