from django.db import models

# Create your models here.


class devicelist(models.Model):
    username = models.CharField(max_length=20)
    passwd = models.CharField(max_length=20)
    url = models.CharField(max_length=20)
    systemUptime = models.CharField(max_length=40)
    serial = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    dn = models.CharField(max_length=30)

class receivelist(models.Model):
    emailaccount = models.CharField(max_length=20)


