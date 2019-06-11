#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 6/4/2019 4:43 AM
# @Author  : Lxz
# @File    : config_vtp.py


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

