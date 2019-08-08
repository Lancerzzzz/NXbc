from django.urls import path
from . import views

urlpatterns = [
    path('getDevice', views.getDevice.as_view(), name='login'),

]
