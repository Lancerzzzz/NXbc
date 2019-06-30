from __future__ import absolute_import, unicode_literals

from django.db import models

from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Widget(models.Model):
    name = models.CharField(max_length=140)
