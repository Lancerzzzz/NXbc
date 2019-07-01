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
    # path('config_trunk/', views.config_trunk.as_view(), name="config_trunk"),
    path('vlan/', views.vlan.as_view(), name="vlan"),
    path('staticroute/', views.staticroute.as_view(), name="staticroute"),
    path('interfaces/', views.interfaces.as_view(), name="interfaces"),
    path('alltrunk/', views.alltrunk.as_view(), name="alltrunk"),
    path('onetrunk/', views.onetrunk.as_view(), name="onetrunk"),
    path('l3allipif/', views.l3allipif.as_view(), name="l3allipif"),
    path('l3oneipif/', views.l3oneipif.as_view(), name="l3oneipif"),
    path('oneint/', views.oneint.as_view(), name="oneint"),

]