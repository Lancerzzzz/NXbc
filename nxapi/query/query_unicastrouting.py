#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    :2019-06-18 15:47
# @Autor   :Zh
# @File    :query_unicastrouting.py
from nxapi.cli_base.cli_base import cli_base
import json


# show ip static-route
def query_staticroute(serial):
    cli = "show ip static-route"
    query = cli_base(serial, cli)
    response = json.loads(query.send().text)
    temp = response['ins_api']['outputs']['output']['body']['TABLE_vrf_all']['ROW_vrf_all']['TABLE_each_vrf']['ROW_each_vrf']
    # print(temp)
    if isinstance(temp,dict):
        temp = [temp]
        static = response['ins_api']['outputs']['output']['body']['TABLE_vrf_all']['ROW_vrf_all']
        # print(static)
        # print(type(static))
        del static["TABLE_each_vrf"]
        # print(static)
        a = [static]
        # print(a)
        a.extend(temp)
        # print(a)
    else:
        static = response['ins_api']['outputs']['output']['body']['TABLE_vrf_all']['ROW_vrf_all']
        del static["TABLE_each_vrf"]
        # print(static)
        a = [static]
        # print(a)
        a.extend(temp)
        # print(a)
    return a
