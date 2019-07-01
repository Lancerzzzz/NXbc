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
from nxapi.query.query_mac import query_allmac
from nxapi.config.config_trunk import Conf_trunk
from nxapi.query.query_intrun import query_oneintru
from nxapi.query.query_intrun import query_allintru
from nxapi.config.config_staticroute import conf_staticroute
from nxapi.query.query_allvlan import query_onevlan
from nxapi.query.query_allvlan import query_vlan
from nxapi.query.query_unicastrouting import query_staticroute
from nxapi.query.query_interface import query_interface_all
from nxapi.query.query_intrun import query_allintru
from nxapi.query.query_intrun import query_oneintru
from nxapi.query.query_l3ipif import query_l3ipif
from nxapi.query.query_l3ipif import query_l3oneipif
from nxapi.query.query_l3ipif import query_l2intbif




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


class mac(View):
    def get(self,request):
        data = query_allmac("9CNTS3XFTXY")
        return JsonResponse(data, safe=False)

    def post(self, request):
        data = query_allmac("9CNTS3XFTXY")
        return JsonResponse(data, safe=False)


class l3ipif(View):

    def get(self,request):
        serial = "9CNTS3XFTXY"
        data = query_l2intbif(serial,'e1/112')
        return JsonResponse(data, safe=False)


class l3allipif(View):

    def get(self,request):
        serial = "9CNTS3XFTXY"
        data = query_l3ipif(serial)
        return JsonResponse(data, safe=False)


class l3oneipif(View):

    def get(self,request):
        serial = "9CNTS3XFTXY"
        eth = 'mgmt0'
        data = query_l3oneipif(serial,eth)
        return JsonResponse(data, safe=False)

class vlan(View):
    def get(self,request):
        serial = "9CNTS3XFTXY"
        fabEncap = "vlan-40"
        name = "hey"
        id="1"
        data = query_onevlan(serial,id)
        return JsonResponse(data, safe=False)


class staticroute(View):

    def get(self,request):
        serial = "9CNTS3XFTXY"
        data = query_staticroute(serial)
        return JsonResponse(data, safe=False)


class interfaces(View):

    def get(self,request):
        serial = "9CNTS3XFTXY"
        data = query_interface_all(serial)
        return JsonResponse(data, safe=False)


class alltrunk(View):

    def get(self,request):
        serial = "9CNTS3XFTXY"
        data = query_allintru(serial)
        return JsonResponse(data, safe=False)


class onetrunk(View):

    def get(self,request):
        serial = "9CNTS3XFTXY"
        eth = 'eth1/112'
        data = query_oneintru(serial,eth)
        return JsonResponse(data, safe=False)


class oneint(View):

    def get(self,request):
        serial = "9CNTS3XFTXY"
        eth = 'eth1/112'
        data = query_l2intbif(serial,eth)
        return JsonResponse(data, safe=False)











