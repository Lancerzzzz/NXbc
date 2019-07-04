#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    :2019-06-13 21:00
# @Autor   :Zh
# @File    :query_l3ipif.py
from nxapi.cli_base.cli_base import cli_base
import json


# ok  show ip int b vrf all
def query_l3ipif(serial):
    cli = "show ip int b vrf all"
    query = cli_base(serial, cli)
    response = json.loads(query.send().text)
    allip = response['ins_api']['outputs']['output']['body']['TABLE_intf']['ROW_intf']
    Vlan = []
    loopback = []
    Ethernet = []
    mgmt = []
    for i in allip:
        if 'Vlan' in i['intf-name']:
            Vlan.append(i)
        elif 'Lo' in i['intf-name']:
            loopback.append(i)
        elif 'Eth' in i['intf-name']:
            Ethernet.append(i)
        elif 'mgmt' in i['intf-name']:
            mgmt.append(i)
    # print(Vlan)
    # print(loopback)
    # print(Ethernet)
    a = {
        "vlan": Vlan,
        "loopback": loopback,
        "ethernet": Ethernet,
        "mgmt": mgmt
    }
    print(a)
    return a


def dict_slice(ori_dict, start, end):
    """
    字典类切片
    :param ori_dict: 字典
    :param start: 起始
    :param end: 终点
    :return:
    """
    slice_dict = {k: ori_dict[k] for k in list(ori_dict.keys())[start:end]}
    return slice_dict


# ok show int mgmt0
def query_l3oneipif(serial,eth):
    cli = "show ip int "+eth
    query = cli_base(serial, cli)
    response = json.loads(query.send().text)
    allip = response['ins_api']['outputs']['output']['body']['TABLE_intf']['ROW_intf']
    allip = dict_slice(allip, 1, 12)
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
