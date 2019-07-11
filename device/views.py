from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse

# Create your views here.
from .models import devicelist
from devicemn import devicemn
from nxapi.cli_base import cli_base
from nxapi.config.config_stp import config_stp
from nxapi.query.query_l3ipif import *
from django.views import View
from nxapi.config.config_stp import config_stp
# from nxapi.query.query_mac import query_l2allmac


def login(request):
    return render(request, "login.html")

class deviceView(View):
    def post(self, request):
        username = str(request.POST["username"])
        password = str(request.POST["passwd"])
        url = str(request.POST["url"])
        devicemn1 = devicemn.devicemn()
        res =devicemn1.add_device(username,password,url)

        return HttpResponse(res)




class home(View):

    def get(self, request):
        d = devicemn.devicemn()
        data = d.get_all_device()
        return render(request, "deviceList.html", {"delist": data})

    def post(self, request):
        name = str(request.POST["username"])
        pwd = str(request.POST["passwd"])
        d = devicemn.devicemn()
        data = d.get_all_device()
        if name != None and not name.__eq__(""):
            if name == "admin" and pwd == "admin":
                return render(request, "home.html", {"delist": data})
            else:
                return HttpResponse(u"passwd or username wrong!!!!")

        else:
            return HttpResponse(u"username can't be empty!!!")


class stp(View):

    def get(self, request):
        a = config_stp("9CNTS3XFTXY", mode="3")
        data = a.config_stpinst()
        return JsonResponse(data, safe=False)

    def post(self, request):
        # serial = str(request.POST["serial"])
        # mode = str(request.POST["mode"])
        serial = "9CNTS3XFTXY"
        mode = "3"
        a = config_stp(serial, mode)
        data = a.config_stpinst()
        return JsonResponse(data, safe=False)


# class mac(View):
#     def get(self, request):
#         data = query_l2allmac("9CNTS3XFTXY")
#         return JsonResponse(data, safe=False)
#
#     def post(self, request):
#         data = query_l2allmac("9CNTS3XFTXY")
#         return JsonResponse(data, safe=False)


class l3ipif(View):

    def get(self, request):
        serial = "9CNTS3XFTXY"
        data = query_l3ipif(serial)
        return JsonResponse(data, safe=False)
