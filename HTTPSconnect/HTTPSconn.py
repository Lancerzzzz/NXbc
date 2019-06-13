#!/usr/bin/python3

# -*- coding: utf-8 -*-
# @Time    : 5/23/2019 3:44 PM
# @Author  : Lxz
import requests, urllib3
import json


class Httpsconn():
    def __init__(self, username, password, ip_addr):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.username = username
        self.password = password
        self.ip_addr = ip_addr
        self.auth_cookie = {}

    def aaa_login(self):
        URL = "https://" + self.ip_addr + "/api/aaaLogin.json"
        PAYLOAD = {
            "aaaUser": {
                "attributes": {
                    "name": self.username,
                    "pwd": self.password
                }
            }
        }
        session = requests.session()
        response = session.post(URL, data=json.dumps(PAYLOAD), verify=False)

        if response.status_code == requests.codes.ok:
            data = json.loads(response.text)['imdata'][0]
            token = str(data['aaaLogin']['attributes']['token'])
            self.auth_cookie = {"APIC-cookie": token}
            return self.auth_cookie
        else:
            return None

    def aaa_logout(self):
        URL = "https://" + self.ip_addr + "/api/aaaLogout.json"
        payload = {
            'aaaUser': {
                'attributes': {
                    'name': self.username
                }
            }
        }
        session = requests.session()
        response = session.post(URL, data=json.dumps(payload), cookies=self.auth_cookie, verify=False)
        return response

    def json_method(self, payload=None, action="GET"):
        URL = "https://" + self.ip_addr + "/api/mo/sys.json"
        session = requests.session()
        response = session.request(action, URL, data=json.dumps(payload), cookies=self.auth_cookie, verify=False)
        return response

    def cli_method(self, cli=""):
        url = 'https://' + self.ip_addr + '/ins'
        payload = {
            "ins_api": {
                "version": "1.0",
                "type": "cli_show",
                "chunk": "0",
                "sid": "1",
                "input": cli,
                "output_format": "json"
            }
        }
        session = requests.Session()
        response = session.post(url, data=json.dumps(payload), auth=(self.username, self.password), verify=False)
        session.close()
        return response

    @staticmethod
    def json_dump(re):
        if isinstance(re, requests.models.Response):
            return json.dumps(json.loads(re.text), indent=2)
        else:
            return None

# a = Httpsconn("admin", "Admin_1234!", "192.168.200.3")
# response = a.cli_method("show ip int e1/1")
# print(response.text)
# res = a.aaa_login()
# pd = {
#     "topSystem": {
#     "children": [
#       {
#         "interfaceEntity": {
#           "children": [
#             {
#               "l1PhysIf": {
#                 "attributes": {
#                     "FECMode": "auto",
#                     "accessVlan": "vlan-10",
#                     "adminSt": "up",
#                     "autoNeg": "on",
#                     "beacon": "off",
#                     "bw": "default",
#                     "childAction": "",
#                     "controllerId": "",
#                     "delay": "1",
#                     "descr": "",
#                     "rn": "phys-[eth1/2]",
#                     "dot1qEtherType": "0x8100",
#                     "duplex": "auto",
#                     "id": "eth1/2",
#                     "inhBw": "4294967295",
#                     "layer": "Layer2",
#                     "linkDebounce": "100",
#                     "linkDebounceLinkUp": "0",
#                     "linkLog": "default",
#                     "linkTransmitReset": "enable",
#                     "mdix": "auto",
#                     "medium": "broadcast",
#                     "mode": "trunk",
#                     "mtu": "1500",
#                     "nativeVlan": "vlan-1",
#                     "persistentOnReload": "true",
#                     "portT": "unknown",
#                     "routerMac": "not-applicable",
#                     "snmpTrapSt": "enable",
#                     "spanMode": "not-a-span-dest",
#                     "speed": "auto",
#                     "speedGroup": "auto",
#                     "status": "",
#                     "trunkLog": "default",
#                     "trunkVlans": "100-110",
#                     "usage": "discovery",
#                     "userCfgdFlags": "admin_layer,admin_state",
#                     "voicePortCos": "none",
#                     "voicePortTrust": "disable",
#                     "voiceVlanId": "none",
#                     "voiceVlanType": "none"
#
#                 }
#               }
#             }
#           ]
#         }
#       }
#     ]
#   }
# }
# # re = a.json_method("/api/mo/sys.json","")
# pd["topSystem"]["children"][0]["interfaceEntity"]["children"][0]["l1PhysIf"]["attributes"].update(accessVlan="vlan-10")
# print(pd)
# re = a.json_method("/api/mo/sys.json", pd, "POST")
#
# print(a.json_dump(re))
# # re = a.json_method("/api/mo/sys/intf/phys-[eth1/4].json?rsp-subtree=children")
# # print(a.json_dump(re))
# re = a.aaa_logout()
# print(a.json_dump(re))
