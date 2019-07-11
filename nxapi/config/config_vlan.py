#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    :${2019/6/15} ${20:00}
# @Autor   :Jbh
# @File    :${config_vlan}.py


from nxapi.config_base.config_base import configbase
import json


class config_vlan():
    def __init__(self, serial,
                 id="e1/1",
                 mode="1",
                 accessVlan="vlan-10",
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
        :param accessVlan:
        DEFAULT: 1
        """
        self.serial = serial
        self.id = id
        self.mode = mode
        self.accessVlan = accessVlan
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
                                            "mode": mode,
                                            "accessVlan": accessVlan
                                        }
                                    }
                                }
                            ]
                        }
                    }
                ]
            }
        }

    def config_ifvlan(self):
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
                                            "mode": self.mode,
                                            "accessVlan": self.accessVlan
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

    def creat_ifvlan(self, fabEncap, name):
        payload = {
            "topSystem": {
                "children": [
                    {
                        "bdEntity": {
                            "children": [
                                {
                                    "l2BD": {
                                        "attributes": {
                                            "fabEncap": fabEncap,
                                            "name": name
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
        return data

    def delete_ifvlan(self, fabEncap, status):
        payload = {
            "topSystem": {
                "children": [
                    {
                        "bdEntity": {
                            "children": [
                                {
                                    "l2BD": {
                                        "attributes": {
                                            "fabEncap": fabEncap,
                                            "status": status
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
        return data
