from nxapi.cli_base.cli_base import cli_base
import json


# ok  show int e1/112 trunk
def query_oneintru(serial, eth):
    cli = "show int " + eth + " trunk"
    query = cli_base(serial, cli)
    response = json.loads(query.send().text)
    one1 = [response['ins_api']['outputs']['output']['body']['TABLE_allowed_vlans']['ROW_allowed_vlans']]
    one2 = [response['ins_api']['outputs']['output']['body']['TABLE_vtp_pruning']['ROW_vtp_pruning']]
    one3 = [response['ins_api']['outputs']['output']['body']['TABLE_stp_forward']['ROW_stp_forward']]
    one4 = [response['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']]
    one1.extend(one2)
    one1.extend(one3)
    one1.extend(one4)
    return one1


# ok show int trunk
def query_allintru(serial):
    cli = "show int trunk"
    query = cli_base(serial, cli)
    response = json.loads(query.send().text)
    allint1 = response['ins_api']['outputs']['output']['body']['TABLE_allowed_vlans']['ROW_allowed_vlans']
    allint2 = response['ins_api']['outputs']['output']['body']['TABLE_vtp_pruning']['ROW_vtp_pruning']
    allint3 = response['ins_api']['outputs']['output']['body']['TABLE_stp_forward']['ROW_stp_forward']
    allint4 = response['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']
    allint1.extend(allint2)
    allint1.extend(allint3)
    allint1.extend(allint4)
    return allint1


# ok  show ip int b
def query_l3ipif(serial):
    cli = "show ip int b"
    query = cli_base(serial, cli)
    response = json.loads(query.send().text)
    allip = response['ins_api']['outputs']['output']['body']['TABLE_intf']['ROW_intf']
    return allip

# ok show int b
def query_l2allintif(serial):
    cli = "show int b"
    query = cli_base(serial, cli)
    response = json.loads(query.send().text)
    allint = response['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']
    return allint


# ok show int e1/112
def query_l2intif(serial,eth):
    cli = "show int "+eth
    query = cli_base(serial, cli)
    response = json.loads(query.send().text)
    allint = response['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']
    return allint


# ok show int e1/112 b
def query_l2intbif(serial,eth):
    cli = "show int " + eth + " b"
    query = cli_base(serial, cli)
    response = json.loads(query.send().text)
    oneintb = response['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']
    return oneintb
