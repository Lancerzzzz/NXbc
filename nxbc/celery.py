from __future__ import absolute_import

import os

import django
from django.conf import settings
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nxbc.settings')
django.setup()
app = Celery('nxbc')
app.config_from_object('django.conf:settings')
print(lambda: settings.INSTALLED_APPS)
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
