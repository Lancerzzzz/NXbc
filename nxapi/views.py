import json

from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from django.views import View
from .query.query_interface import query_interface_all
from device.models import devicelist
from nxapi.query.query_mac import query_onemac


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
