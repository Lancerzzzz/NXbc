#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 6/4/2019 3:50 AM
# @Author  : Lxz
# @File    : config_stp.py

from nxapi.config_base.config_base import configbase
import json


class config_stp():
    def __init__(self, serial,
                 adminSt=" 1",
                 mode="1",
                 bridge="1",
                 ctrl="1",
                 fcoe="1",
                 l2GStpDomId="1024",
                 loopguard="1",
                 pathcostOp="1"
                 ):
        """
        :param serial: "" Serial number defines unique device
        :param adminSt:
                        1 - enabled
                        2 - disabled
                        DEFAULT: enabled
                        The administrative state of the object or policy.
        :param mode:
                        1 - mst
                        2 - pvrst
                        DEFAULT: pvrst
                        stp mode

        :param bridge:
                        1 - enabled
                        2 - disabled
                        DEFAULT: enabled
                        enable spanning-tree bridge assurance on all ports
        :param ctrl:
                        1 - stateful-ha
                        DEFAULT: normal
                        The control state.

        :param fcoe:
                        1 - enabled
                        2 - disabled
                        DEFAULT: enabled
                        enable spanning tree for fcoe vlan
        :param l2GStpDomId:
                        [0 , 200000000]
                        DEFAULT: 1024
                        spanning tree L2 Gateway Domain Id
        :param loopguard:
                        1 - enabled
                        2 - disabled
                        DEFAULT: disabled
                        enable loop guard on all ports
        :param pathcostOp:
                        0 - auto
                        1 - short
                        2 - long
                        DEFAULT: short
                        Spanning tree pathcost options
        """
        self.serial = serial
        self.adminSt = adminSt
        self.mode = mode
        self.bridge = bridge
        self.ctrl = ctrl
        self.fcoe = fcoe
        self.l2GStpDomId = l2GStpDomId
        self.loopguard = loopguard
        self.pathcostOp = pathcostOp
        self.payload = {
                    "topSystem": {
                        "children": [
                            {
                                "stpEntity": {
                                    "children": [
                                        {
                                            "stpInst": {
                                                "attributes": {
                                                    "adminSt": adminSt,
                                                    "bridge": bridge,
                                                    "ctrl": ctrl,
                                                    "fcoe": fcoe,
                                                    "l2GStpDomId": l2GStpDomId,
                                                    "loopguard": loopguard,
                                                    "mode": mode,
                                                    "pathcostOp": pathcostOp,
                                                }
                                            }
                                        }
                                    ]
                                }
                            }
                        ]
                    }
                }

    def config_stpinst(self):
        payload = {
                    "topSystem": {
                        "children": [
                            {
                                "stpEntity": {
                                    "children": [
                                        {
                                            "stpInst": {
                                                "attributes": {
                                                    "mode": self.mode
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
        data = json.loads(response.text)
        return data
        # if len(data) == 0:
        #     return True
        # else:
        #     return False

    def config_stpif(self,):
        pass

    def config_stp_mstentity(self,
                             adminSt="1",
                             fwdtime="15",
                             helloTime="2",
                             maxAge="20",
                             maxHops="20",
                             regName="",
                             rev="0",
                             simulate="1"
                             ):
        """
        :param adminSt: Admin State
                        1 - enabled
                        2 - disabled
                        DEFAULT: enabled

        :param fwdtime:STP forward delay
                        RANGE: [4 , 30]
                        DEFAULT: 15

        :param helloTime:STP Hello interval
                        RANGE: [1 , 10]
                        DEFAULT: 2

        :param maxAge:STP max age interval
                        RANGE: [6 , 40]
                        DEFAULT: 20

        :param maxHops:STP mst max hops
                        RANGE: [1 , 255]
                        DEFAULT: 20

        :param regName:Region Name
                        MAX SIZE: 32
                        DEFAULT:""

        :param rev:Region Revision
                        RANGE: [0 , 0xffff]
                        DEFAULT: 0
        :param simulate:spanning tree simulation
                        1 - enabled
                        2 - disabled
                        DEFAULT: enabled
        :return: bool
        """
        payload = {
                "topSystem": {
                    "children": [
                        {
                            "stpEntity": {
                                "children": [
                                    {
                                        "stpInst": {
                                            "attributes": {
                                                "mode": "mst"
                                            },
                                            "children": [
                                                {
                                                    "stpMstEntity": {
                                                        "attributes": {
                                                                "adminSt": adminSt,
                                                                "fwdTime": fwdtime,
                                                                "helloTime": helloTime,
                                                                "maxAge": maxAge,
                                                                "maxHops": maxHops,
                                                                "regName": regName,
                                                                "rev": rev,
                                                                "simulate": simulate,
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


    def config_stp_mstdom(self,name):

        pass
