#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 5/26/2019 3:14 PM
# @Author  : Lxz
# @File    : devicemn.py

from device.models import devicelist
from HTTPSconnect import HTTPSconn
import json


class devicemn():

    def get_all_device(self):
        resuelt = list(devicelist.objects.all().values())
        return resuelt

    def get_deviceinfo(self, serial):
        resurlut = devicelist.objects.get(serial=serial)
        return resurlut

    def  add_device(self, username, passwd, url):
        con = HTTPSconn.Httpsconn(username, passwd, url)
        con.aaa_login()
        response = con.json_method()
        data = json.loads(response.text)['imdata'][0]['topSystem']['attributes']
        # print(json.dumps(data, indent=2))
        devicelist.objects.create(
                                    username=username,
                                    passwd=passwd,
                                    url=url,
                                    serial=data['serial'],
                                    systemUptime=data['systemUpTime'],
                                    status=data['status'],
                                    dn=data['dn']

            )
        return True




