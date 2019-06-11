#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 5/26/2019 3:55 PM
# @Author  : Lxz
# @File    : forms.py

from django import forms

class loginform(forms.Form):

    username = forms.CharField()
    passwd   = forms.CharField()