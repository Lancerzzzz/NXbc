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
                 prefix = "",
                 nhAddr = "",
                 nhIf = "",
                 nhVrf = "default",
                 object1 = " ",
                 pref = "",
                 rtname = "",
                 tag = ""
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
        self.nhIf = nhIf
        self.nhVrf = nhVrf
        self.object1 = object1
        self.pref = pref
        self.rtname = rtname
        self.tag = tag
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
                                                                                "nhIf": nhIf,
                                                                                "nhVrf": nhVrf,
                                                                                "object": object1,
                                                                                "pref": pref,
                                                                                "rtname": rtname,
                                                                                "tag": tag
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
                                                                                "nhIf": self.nhIf,
                                                                                "nhVrf": self.nhVrf,
                                                                                "object": self.object1,
                                                                                "pref": self.pref,
                                                                                "rtname": self.rtname,
                                                                                "tag": self.tag
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
        config = configbase(self.serial, payload)
        response = config.send()
        data = json.loads(response.text)
        return data
