import json

from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from django.views import View
from .query.query_interface import query_interface_all
from device.models import devicelist
from nxapi.query.query_mac import query_allmac
from nxapi.query.query_route import query_route_all
from .config import config_ip, config_vlan, config_trunk
from .query import query_allvlan


class routeView(View):
    def get(self, request):
        # serial = "9CNTS3XFTXY"
        # eth = "Vlan103"
        eth = "e1/5"
        # data = query_allmac(serial)
        # print("data:", data)
        # data= json.dumps(data)
        return render(request, "queryRoute.html", {"data": "test"})
        # return JsonResponse(data, safe=False)

    def post(self, request):
        serial = request.POST['serial']
        data = query_route_all(serial)
        return JsonResponse(data, safe=False)

class mac(View):
    def get(self, request):
        serial = "9CNTS3XFTXY"
        # eth = "Vlan103"
        eth = "e1/5"
        data = query_allmac(serial)
        print("data:", data)
        data= json.dumps(data)
        return render(request, "queryMac.html", {"data": data})
        # return JsonResponse(data, safe=False)

    def post(self, request):
        serial = "9CNTS3XFTXY"
        eth = "e1/5"
        data = query_allmac(serial)
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
        confIP = config_ip.config_ip(serial, eth, ip)
        info = confIP.config_ipv4()
        return HttpResponse(info)


class vlanView(View):
    def get(self, request):
        data = query_allvlan.query_vlan("9CNTS3XFTXY")
        data = json.dumps(data)
        print("data:", data)
        return render(request, "queryVlan.html", {"data": data})

    def post(self, request):
        serial = str(request.POST["serial"])
        print("Vlan view's serial:", serial)
        data = query_allvlan.query_vlan(serial)
        data = json.dumps(data)
        print("data:", data)
        return JsonResponse(data, safe=False)


class accessConfigView(View):
    def get(self, request):
        return render(request, "accessVlan.html", {"test": "test"})

    def post(self, request):
        serial = str(request.POST["serial"])
        eth = str(request.POST["eth"])
        vlan = str(request.POST["vlan"])
        confVlan = config_vlan.config_vlan(serial, eth, "1", vlan)
        info = confVlan.config_ifvlan()
        return HttpResponse(info)


class confTrunk(View):
    def get(self, request):
        return render(request, "confTrunk.html", {"test": "test"})

    def post(self, request):
        serial = str(request.POST["serial"])
        eth = str(request.POST["eth"])
        vlanRange = str(request.POST['vlanRange'])
        nativeVlan = str(request.POST["nativeVlan"])
        configTrunk = config_trunk.Conf_trunk(serial, eth, vlanRange, nativeVlan)
        info = configTrunk.config_trunk()
        print("info:", info)
        return HttpResponse(info)
