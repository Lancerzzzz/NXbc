from nxapi.cli_base.cli_base import cli_base
import json


def query_allip(serial):
    cli = "show ip interface brief"   # 命令
    query = cli_base(serial, cli)   # cli_base()形成查询环境
    response = json.loads(query.send().text)     # 发送请求 request
    data = response['ins_api']['outputs']['output']['body']['TABLE_intf']['ROW_intf']
    return data

def query_oneip(serial, eth):
    # e1/5
    cli = "show run interface " + eth   # 命令
    query = cli_base(serial, cli)   # cli_base()形成查询环境
    response = json.loads(query.send().text)     # 发送请求 request
    data = response['ins_api']['outputs']['output']['body']['nf:filter']['m:configure']['m:terminal']['interface']['__XML__PARAM__interface']
    return data
