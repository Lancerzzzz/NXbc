from nxapi.cli_base.cli_base import cli_base
import json

# eth = eth1/5
# query_mac(serial)
# query_mac(serial, eth)
# data[0] -- Ethernet
# data[1] -- Vlan
def query_onemac(serial, *eth):
    if len(eth) == 0:
        cli = "show int mac"
    else:
        cli = "show int " + eth[0] + " mac"
    query = cli_base(serial, cli)
    response = json.loads(query.send().text)
    onemac = response['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']
    EthernetLi = []
    VlanLi = []
    for s in onemac:
        str = s['interface']
        if str[0] == 'E' and str[1] == 't' and str[2] == 'h':
            EthernetLi.append(s)
        elif str[0] == 'V' and str[1] == 'l' and str[2] == 'a':
            VlanLi.append(s)
    li = []
    li.append(EthernetLi)
    li.append(VlanLi)
    return li
