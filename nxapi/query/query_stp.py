#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 6/12/2019 6:59 AM
# @Author  : Lxz
# @File    : query_stp.py

from nxapi.cli_base.cli_base import cli_base


class query_stp():
    def __init__(self, serial):
        self.serial = serial
