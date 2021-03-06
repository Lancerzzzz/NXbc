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
    path('home/', views.home.as_view(), name="home"),
    path('stp/', views.stp.as_view(), name="stp"),
    path('mac/', views.mac.as_view(), name="mac"),
    path('l3ipif/', views.l3ipif.as_view(), name="l3ipif"),
    path('vlan/', views.vlan.as_view(), name="vlan"),
    path('sendmail/', views.sendmail.as_view(), name="sendmail"),
    path('receiveList/', views.test.as_view(), name="receiveList"),
    path('delTar/',views.delTar.as_view(), name="delTar"),
    path('createTar/',views.createTar.as_view(), name='createTar')
]
