from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.first_celery, name="task"),
]
