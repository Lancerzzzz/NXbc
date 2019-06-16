#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    :2019/6/13 21:19
# @Autor   :Lsr
# @File    :config_ip.py

from nxapi.config_base.config_base import configbase
import json

"""
使用方法：
a = config_ip(serial, name, eth, addr)
a.config_ipv4()
其中eth = "eth1/1"这种形式Not e1/1
addr = "10.10.10.1/10"这种形式
"""

class config_ip():
    def __init__(self, serial, name, eth, addr):
        self.serial = serial
        self.name = name
        self.eth = eth
        self.addr = addr    # addr = '10.10.10.1/10'
        self.payload = {
            "topSystem": {
                "children": [{
                    "ipv4Entity": {
                        "children": [{
                            "ipv4Inst": {
                                "children": [{
                                    "ipv4Dom": {
                                        "attributes": {
                                            "name": name
                                        },
                                        "children": [{
                                            "ipv4If": {
                                                "attributes": {
                                                    "id": eth
                                                },
                                                "children": [{
                                                    "ipv4Addr": {
                                                        "attributes": {
                                                            "addr": addr
                                                        }
                                                    }
                                                }]
                                            }
                                        }]
                                    }
                                }]
                            }
                        }]
                    }
                }]
            }
        }

    def config_ipv4(self):
        config = configbase(self.serial, self.payload)
        response = config.send()
        data = json.loads(response.text)['imdata']
        return data
