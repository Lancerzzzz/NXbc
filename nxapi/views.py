import json

from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from django.views import View
from .query.query_interface import query_interface_all
from device.models import devicelist
from nxapi.query.query_mac import query_onemac
from .config import config_ip
from .config import config_ip
from .query import query_allvlan


class mac(View):
    def get(self, request):
        serial = "9CNTS3XFTXY"
        # eth = "Vlan103"
        eth = "e1/5"
        data = query_onemac(serial, eth)
        print("data:", data)
        return JsonResponse(data, safe=False)

    def post(self, request):
        serial = "9CNTS3XFTXY"
        eth = "e1/5"
        data = query_onemac(serial, eth)
        return JsonResponse(data, safe=False)


class interface(View):
    def get(self, request):
        return render(request, "queryInt.html", {"test": "test"})


class queryInterface(View):
    def get(self, request):
        return HttpResponse("这是get方法")

    def post(self, request):
        serial = request.POST['serial']
        print("serial:", serial)
        info = query_interface_all(serial)
        # print(info)
        return JsonResponse(info, safe=False)


class queryDevice(View):
    def post(self, request):
        result = devicelist.objects.values("serial")
        deviceSerial = []
        serialList = {}
        print(result)
        for i in result:
            print(i)
            if i['serial']:
                deviceSerial.append(i['serial'])
        print("deviceSerial:", deviceSerial)
        serialList['serial'] = deviceSerial
        # json.dump(serialList)
        return JsonResponse(serialList, safe=False)

    def get(self, request):
        result = devicelist.objects.values_list("serial")
        # result = {'device':result}
        # print(result)
        return JsonResponse(result, safe=False)


class ipView(View):
    def get(self, request):
        return render(request, "confIP.html", {"test": "test"})


class ipConf(View):
    def post(self, request):
        serial = str(request.POST["serial"])
        eth = str(request.POST["eth"])
        # eth = "eth1/118"
        ip = str(request.POST['ip'])
        print("eth:", eth, "serial:", serial, "ip:", ip)
        confIP = config_ip.config_ip(serial,  eth, ip)
        info = confIP.config_ipv4()
        return HttpResponse(info)

class vlanView(View):
    def get(self, request):
        data = query_allvlan.query_vlan("9CNTS3XFTXY")
        return render(request, "queryVlan.html", {"data": data})

