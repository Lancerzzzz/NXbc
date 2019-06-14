from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse

# Create your views here.
from .models import devicelist
from devicemn import devicemn
from nxapi.cli_base import cli_base
from nxapi.config.config_stp import config_stp
from nxapi.query.query_l3ipif import *
from  django.views import  View
from nxapi.config.config_stp import config_stp
from nxapi.query.query_mac import query_l2allmac
from nxapi.config.config_trunk import Conf_trunk


def login(request):
    return render(request, "login.html")


# def home(request):
#     if request.method == "POST":
#         name = str(request.POST["username"])
#         pwd = str(request.POST["passwd"])
#
#         d = devicemn.devicemn()
#
#
#         # 查询设备的测试，供参考
#         re = d.get_deviceinfo("9GBPQALUKDY")
#         print(re.username)
#         print(re.passwd)
#         print(re.url)
#         print(re.serial)
#         print(re.systemUptime)
#
#         # 添加设备的测试语句 需要正确的信息才能执行，供参考
#         data = d.add_device("admin", "Admin_1234!", "sbx-nxos-mgmt.cisco.com")
#
#         data = d.get_all_device()
#
#
#         # cli_命令执行测试
#         c = cli_base.cli_base("9GBPQALUKDY", "show version")
#
#         a = config_stp("9GBPQALUKDY", mode="3")
#         data = a.config_stp_mode()
#         data = query_allintru("9CNTS3XFTXY")
#         data = query_l2intbif("9CNTS3XFTXY","e1/5")
#         data = query_allintru("9CNTS3XFTXY")
#         data = query_l3ipif("9CNTS3XFTXY")
#
#
#
#         if name != None and not name.__eq__(""):
#             if name == "admin" and pwd == "admin":
#                 return JsonResponse(data, safe=False)
#             else:
#                 return HttpResponse(u"passwd or username wrong!!!!")
#
#         else:
#             return HttpResponse(u"username can't be empty!!!")
#         return


class home(View):

    def get(self, request):
        return HttpResponse('Hello, World!get')

    def post(self, request):
        name = str(request.POST["username"])
        pwd = str(request.POST["passwd"])
        d = devicemn.devicemn()
        data = d.get_all_device()
        if name != None and not name.__eq__(""):
            if name == "admin" and pwd == "admin":
                return render(request, "home.html",{"delist":data})
            else:
                return HttpResponse(u"passwd or username wrong!!!!")

        else:
            return HttpResponse(u"username can't be empty!!!")


class stp(View):

    def get(self, request):
        a = config_stp("9CNTS3XFTXY", mode="3")
        data = a.config_stpinst()
        return JsonResponse(data,safe=False)

    def post(self, request):
        # serial = str(request.POST["serial"])
        # mode = str(request.POST["mode"])
        serial = "9CNTS3XFTXY"
        mode = "3"
        a = config_stp(serial, mode)
        data = a.config_stpinst()
        return JsonResponse(data,safe=False)


class config_trunk(View):

    def get(self,request):
        serial = "9CNTS3XFTXY"
        id = "eth1/111"
        mode = "2"
        trunkVlans = "10-20"
        config = Conf_trunk(serial,id,mode,trunkVlans)
        data = config.config_trunk()
        return HttpResponse(json.dumps(data))

class mac(View):
    def get(self,request):
        data = query_l2allmac("9CNTS3XFTXY")
        return JsonResponse(data, safe=False)

    def post(self, request):
        data = query_l2allmac("9CNTS3XFTXY")
        return JsonResponse(data, safe=False)


class l3ipif(View):

    def get(self,request):
        serial = "9CNTS3XFTXY"
        data = query_l2intbif(serial,'e1/112')
        return JsonResponse(data, safe=False)







