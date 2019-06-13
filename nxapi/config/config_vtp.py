#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 6/4/2019 4:43 AM
# @Author  : Lxz
# @File    : config_vtp.py
from nxapi.config_base.config_base import configbase
import json


class config_vtp():
    def __init__(self, serial, adminSt, domain, password, version):
        self.serial = serial
        self.adminSt = adminSt
        self.domain = domain
        self.password = password
        self.version = version
        self.payload ={
                      "topSystem": {
                        "children": [
                          {
                            "vtpEntity": {
                              "children": [
                                {
                                  "vtpInst": {
                                    "attributes": {
                                      "domain": "ccie",
                                      "password": "ccie",
                                      "version": "2"
                                    }
                                  }
                                }
                              ]
                            }
                          },
                          {
                            "fmEntity": {
                              "children": [
                                {
                                  "fmVtp": {
                                    "attributes": {
                                      "adminSt": "enabled"
                                    }
                                  }
                                }
                              ]
                            }
                          }
                        ]
                      }
                    }

    def config_vtp_info(self):
        config = configbase(self.serial, self.payload)
        response = config.send()
        data = json.loads(response.text)
        return data


