#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 6/4/2019 3:53 AM
# @Author  : Lxz
# @File    : config_base.py

from device.models import devicelist
from HTTPSconnect.HTTPSconn import Httpsconn


class configbase():
    def __init__(self, serial, payload):
        self.serial = serial
        self.payload = payload

    def send(self):
        device = devicelist.objects.get(serial=self.serial)
        con = Httpsconn(device.username, device.passwd, device.url)
        con.aaa_login()
        response = con.json_method(self.payload, "POST")
        con.aaa_logout()
        return response
