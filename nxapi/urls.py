from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('mac/', views.mac.as_view(), name='mac'),
    path('interface/', views.interface.as_view(), name='interface'),
    path('queryDevice/', views.queryDevice.as_view(), name='queryDevice'),
    path('queryInterface/', views.queryInterface.as_view(), name='queryInterface')
]
