#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    :2019-06-14 11:00
# @Autor   :Zh
# @File    :query_intrun.py

from nxapi.cli_base.cli_base import cli_base
import json


# ok  show int e1/112 trunk
def query_oneintru(serial, eth):
    cli = "show int " + eth + " trunk"
    query = cli_base(serial, cli)
    response = json.loads(query.send().text)
    one1 = response['ins_api']['outputs']['output']['body']['TABLE_allowed_vlans']['ROW_allowed_vlans']
    one2 = response['ins_api']['outputs']['output']['body']['TABLE_vtp_pruning']['ROW_vtp_pruning']
    one3 = response['ins_api']['outputs']['output']['body']['TABLE_stp_forward']['ROW_stp_forward']
    one4 = response['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']
    one = {}
    one.update(one1)
    one.update(one2)
    one.update(one3)
    one.update(one4)
    return one


# ok show int trunk
def query_allintru(serial):
    cli = "show int trunk"
    query = cli_base(serial, cli)
    response = json.loads(query.send().text)
    allint1 = response['ins_api']['outputs']['output']['body']['TABLE_allowed_vlans']['ROW_allowed_vlans']
    allint2 = response['ins_api']['outputs']['output']['body']['TABLE_vtp_pruning']['ROW_vtp_pruning']
    allint3 = response['ins_api']['outputs']['output']['body']['TABLE_stp_forward']['ROW_stp_forward']
    allint4 = response['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']
    for i in range(0, len(allint1)):
        allint1[i].update(allint2[i])
        allint1[i].update(allint3[i])
        allint1[i].update(allint4[i])
    return allint1

