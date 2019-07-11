#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    :2019-06-13 20:34
# @Autor   :Zh
# @File    :config_trunk.py
from nxapi.config_base.config_base import configbase
import json


class Conf_trunk():
    def __init__(self, serial,
                 id="e1/1",
                 trunkVlans="1-4094",
                 nativeVlan="vlan-1"
                 ):
        """

        :param serial:
        :param id:
        Must match first field in the output of show intf brief. Example: Eth1/1 or Vlan100
        :param mode:
        SELECTION:
        1 - access
        2 - trunk
        3 - fex-fabric
        4 - dot1q-tunnel
        5 - promiscuous
        6 - host
        7 - trunk_secondary
        8 - trunk_promiscuous
        DEFAULT: access
        :param trunkVlans:
        DEFAULT: 1-4094
        :param nativeVlan:
        SELECTION: unknown, vlan-%d or vxlan-%d DEFAULT: vlan-1
        """
        self.serial = serial
        self.id = id
        self.trunkVlans = trunkVlans
        self.nativeVlan = nativeVlan
        self.payload = {
            "topSystem": {
                "children": [
                    {
                        "interfaceEntity": {
                            "children": [
                                {
                                    "l1PhysIf": {
                                        "attributes": {
                                            "id": id,
                                            "mode": "2",
                                            "trunkVlans": trunkVlans,
                                            "nativeVlan": nativeVlan
                                        }
                                    }
                                }
                            ]
                        }
                    }
                ]
            }
        }

    def config_trunk(self):
        payload = {
            "topSystem": {
                "children": [
                    {
                        "interfaceEntity": {
                            "children": [
                                {
                                    "l1PhysIf": {
                                        "attributes": {
                                            "id": self.id,
                                            "mode": "2",
                                            "trunkVlans": self.trunkVlans,
                                            "nativeVlan": self.nativeVlan
                                        }
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
        data = json.loads(response.text)['imdata']
        print("data:", data)
        if not data:
            return True
        else:
            return False
