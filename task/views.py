from django.http import HttpResponse
from django.shortcuts import render
from .tasks import first_task


# Create your views here.

def first_celery(req):
    # 任务参数名.delay(参数)
    # first_task.delay(4)
    print("test")
    return HttpResponse("ok")
