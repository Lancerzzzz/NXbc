#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    :2019-06-13 21:00
# @Autor   :Zh
# @File    :query_l3ipif.py
from nxapi.cli_base.cli_base import cli_base
import json


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
