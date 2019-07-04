from django.contrib import admin

from . import models
# Register your models here.
admin.site.register(models.devicelist)
admin.site.register(models.receivelist)