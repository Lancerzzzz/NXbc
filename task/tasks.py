# Create your tasks here
from __future__ import absolute_import, unicode_literals

import time

from celery import shared_task
from celery import task
from celery.schedules import crontab
from celery import Celery
from celery.task import periodic_task
from django.http import HttpResponse

from task.models import Widget

app = Celery(__name__)
print(__name__)
# app.config_from_object('celeryconfig')


# @periodic_task(run_every=10)
# @app.task
@shared_task
def first_task(loopnum):
    # 模拟一个耗时操作
    for i in range(2):
        time.sleep(2)
        print("test")
    return {"OK": 1}
