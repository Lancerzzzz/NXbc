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
