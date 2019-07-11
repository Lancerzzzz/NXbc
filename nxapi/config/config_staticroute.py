#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    :2019-06-18 15:46
# @Autor   :Zh
# @File    :config_staticroute.py

from nxapi.config_base.config_base import configbase
import json


# ip route 192.168.10.0/24 e 1/111 192.168.10.22 vrf aa name sta5 tag 1234 1
class conf_staticroute():
    def __init__(self, serial,
                 prefix="",
                 nhAddr="",
                 nhVrf="default",
                 ):
        """

        :param serial:
                    Serial number defines unique device
        :param prefix:
                    Value must match ipv4 or ipv6 known format
        :param nhAddr:
                    Value must match ipv4 or ipv6 known format
        :param nhIf:
                    Value must match ipv4 or ipv6 known format
        :param nhVrf:
                    A sequence of characters
        :param object1:
                    RANGE: [0, 4294967295]
        :param pref:
                    RANGE: [0, 255]
        :param rtname:
                    A sequence of characters
        :param tag:
                    RANGE: [0, 4294967295]
        """
        self.serial = serial
        self.prefix = prefix
        self.nhAddr = nhAddr
        self.nhVrf = nhVrf
        self.payload = {
            "topSystem": {
                "children": [
                    {
                        "ipv4Entity": {
                            "children": [
                                {
                                    "ipv4Inst": {
                                        "children": [
                                            {
                                                "ipv4Dom": {
                                                    "attributes": {
                                                        "name": "default"
                                                    },
                                                    "children": [
                                                        {
                                                            "ipv4Route": {
                                                                "attributes": {
                                                                    "prefix": prefix
                                                                },
                                                                "children": [
                                                                    {
                                                                        "ipv4Nexthop": {
                                                                            "attributes": {
                                                                                "nhAddr": nhAddr,
                                                                                "nhVrf": nhVrf,
                                                                                "nhIf": "unspecified",
                                                                                "object" : "0"
                                                                            }
                                                                        }
                                                                    }
                                                                ]
                                                            }
                                                        }
                                                    ]
                                                }
                                            }
                                        ]
                                    }
                                }
                            ]
                        }
                    }
                ]
            }
        }

    def config_staticroute1(self):
        payload = {
            "topSystem": {
                "children": [
                    {
                        "ipv4Entity": {
                            "children": [
                                {
                                    "ipv4Inst": {
                                        "children": [
                                            {
                                                "ipv4Dom": {
                                                    "attributes": {
                                                        "name": "default"
                                                    },
                                                    "children": [
                                                        {
                                                            "ipv4Route": {
                                                                "attributes": {
                                                                    "prefix": self.prefix
                                                                },
                                                                "children": [
                                                                    {
                                                                        "ipv4Nexthop": {
                                                                            "attributes": {
                                                                                "nhAddr": self.nhAddr,
                                                                                "nhVrf": self.nhVrf,
                                                                            }
                                                                        }
                                                                    }
                                                                ]
                                                            }
                                                        }
                                                    ]
                                                }
                                            }
                                        ]
                                    }
                                }
                            ]
                        }
                    }
                ]
            }
        }
        config = configbase(self.serial, self.payload)
        response = config.send()
        data = json.loads(response.text)["imdata"]
        if not data:
            return True
        else:
            return False
