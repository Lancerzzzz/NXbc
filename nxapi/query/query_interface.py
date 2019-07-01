#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    :2019/6/13 21:19
# @Autor   :Lsr
# @File    :config_ip.py

from nxapi.cli_base.cli_base import cli_base
import json

def query_interface(serial, *eth):
    if len(eth) == 0:
        cli = "show interface brief"
    else:
        cli = "show interface " + eth[0]
    query = cli_base(serial, cli)
    response = json.loads(query.send().text)
    data = response['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']
    return data
