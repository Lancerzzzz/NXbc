#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 6/4/2019 2:55 AM
# @Author  : Lxz
# @File    : cli_base.py

from device.models import devicelist
from HTTPSconnect.HTTPSconn import Httpsconn


class cli_base():
    def __init__(self, serial, cli):
        self.serial = serial
        self.cli = cli

    def send(self):
        device = devicelist.objects.get(serial=self.serial)
        con = Httpsconn(device.username, device.passwd, device.url)
        return con.cli_method(self.cli)
