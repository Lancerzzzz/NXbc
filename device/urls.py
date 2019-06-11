#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 5/26/2019 3:46 PM
# @Author  : Lxz
# @File    : urls.py

from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home),
]