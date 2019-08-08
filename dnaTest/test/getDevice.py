
import requests
import json
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth

url1 = 'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token'
url2 = 'https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device'
myusername = 'devnetuser'
mypassword = 'Cisco123!'

def get_token():
    token = requests.post(url1, auth=HTTPBasicAuth(myusername,mypassword),
                          headers={'content-type':'application/json'},
                          verify=False,
                          )
    data1 = token.json()
    print(data1)
    return data1['Token']

def get_devices(ticket):
    n = 0
    payload = ''
    newheaders = {
        'X-Auth-Token': ticket,
        'cache-control': 'no-cache'
        }
    response = requests.request('GET', url2, data=payload, headers=newheaders)
    data2 = response.json()
    print(json.dumps(data2,indent=4,separators=(',',':')))
    for i in data2['response']:
        if i['reachabilityStatus']== 'Reachable':
            n+=1
            print('{:30}'.format(i['hostname']) + ' ' +'{:50}'.format(i['series']) + ' ' + i['managementIpAddress'] )
    print('Total %d reachable devices' %n)

ticket = get_token()
get_devices(ticket)
