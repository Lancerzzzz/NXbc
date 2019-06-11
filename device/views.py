from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse

# Create your views here.
from .models import devicelist
from devicemn import devicemn
from nxapi.cli_base import cli_base
from nxapi.config.config_stp import config_stp
from nxapi.query.query_l3ipif import *


def login(request):
    return render(request, "login.html")


def home(request):
    if request.method == "POST":
        name = str(request.POST["username"])
        pwd = str(request.POST["passwd"])

        # d = devicemn.devicemn()


        #查询设备的测试，供参考
        # re = d.get_deviceinfo("9GBPQALUKDY")
        # print(re.username)
        # print(re.passwd)
        # print(re.url)
        # print(re.serial)
        # print(re.systemUptime)

        # 添加设备的测试语句 需要正确的信息才能执行，供参考
        # data = d.add_device("admin", "Admin_1234!", "sbx-nxos-mgmt.cisco.com")

        # data = d.get_all_device()


        #cli_命令执行测试
        # c = cli_base.cli_base("9GBPQALUKDY", "show version")

        # a = config_stp("9GBPQALUKDY", mode="3")
        # data = a.config_stp_mode()
        # data = query_allintru("9CNTS3XFTXY")
        # data = query_l2intbif("9CNTS3XFTXY","e1/5")
        # data = query_allintru("9CNTS3XFTXY")
        data = query_l3ipif("9CNTS3XFTXY")



        if name != None and not name.__eq__(""):
            if name == "admin" and pwd == "admin":
                return JsonResponse(data, safe=False)
            else:
                return HttpResponse(u"passwd or username wrong!!!!")

        else:
            return HttpResponse(u"username can't be empty!!!")
        return






