from django.contrib.sites import requests
import json
from django.http import HttpResponse
from django.shortcuts import render
import requests as req
from django.views import View
from requests.auth import HTTPBasicAuth


class getDevice(View):
    # def __init__(self):
    #     self.url1 = 'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token'
    #     self.url2 = 'https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device'
    #     self.myusername = 'devnetuser'
    #     self.mypassword = 'Cisco123!'

    def get(self, request):
        def get_token():
            token = req.post('https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token',
                             auth=HTTPBasicAuth('devnetuser', 'Cisco123!'),
                             headers={'content-type': 'application/json'},
                             verify=False,
                             )
            data1 = token.json()
            return data1['Token']

        def get_devices(ticket):
            n = 0
            payload = ''
            newheaders = {
                'X-Auth-Token': ticket,
                'cache-control': 'no-cache'
            }
            response = req.request('GET', 'https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device',
                                   data=payload, headers=newheaders)
            data2 = response.json()
            print(json.dumps(data2, indent=4, separators=(',', ':')))
            for i in data2['response']:
                if i['reachabilityStatus'] == 'Reachable':
                    n += 1
                    print(
                        '{:30}'.format(i['hostname']) + ' ' + '{:50}'.format(i['series']) + ' ' + i[
                            'managementIpAddress'])
            print('Total %d reachable devices' % n)
            return data2

        print("111")
        ticket = get_token()
        deviceInfo = get_devices(ticket)
        return HttpResponse(deviceInfo)

    def post(self, request):
        name = str(request.POST["username"])
        pwd = str(request.POST["passwd"])
        if name != None and not name.__eq__(""):
            if name == "admin" and pwd == "admin":
                return render(request, "home.html", {"test": "test"})
            else:
                return HttpResponse("0")
        else:
            return HttpResponse('0')
