from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('mac/', views.mac.as_view(), name='mac'),
    path('interface/', views.interface.as_view(), name='interface'),
    path('queryDevice/', views.queryDevice.as_view(), name='queryDevice'),
    path('queryInterface/', views.queryInterface.as_view(), name='queryInterface'),
    path('ipView/', views.ipView.as_view(), name='ipVIew'),
    path('ipConf/', views.ipConf.as_view(), name="confIP"),
    path('vlanView/', views.vlanView.as_view(), name="vlanView"),
    path('queryVlan/', views.queryVlan.as_view(), name="queryVlan"),
    path('accessConfigView/', views.accessConfigView.as_view(), name="accessConfigView"),
    path('confTrunk/', views.confTrunk.as_view(), name="confTrunk"),
    path('queryMac/', views.mac.as_view(), name="queryMac"),
    path('queryRoute/', views.routeView.as_view(), name="queryRoute"),
    path('confStp/', views.confStp.as_view(), name="confStp"),
    path('staticRoute/', views.staticRouteView.as_view(), name="staticRoute"),

]
