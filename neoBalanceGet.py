# -*- coding: utf-8 -*-

import requests
import json


def dataGet(address):

    print ("NEO address: ", end="")
    print(address)
    # neoscan
    url = 'https://neoscan.io/'

    #APIextention
    NeoGetBalance='api/main_net/v1/get_balance/'
    NeoGetHight='api/main_net/v1/get_height/'

    # urlの作成
    paramStrB = url+NeoGetBalance+address
    paramStrH = url+NeoGetHight

    response= requests.get(paramStrB)
    content = response.json()

    #特定のキーの残高の抽出
    for key in content['balance']:
        if key['asset'] == "NEO":
                    print("NEO Balance is ",key['amount']),

    response= requests.get(paramStrH)
    content = response.json()
    print("Block Heihgt is ",content['height']),

    print("------------------")

if __name__ == '__main__':

    #NEO Address
    address1='AXDt2hzT35knLnV3MB3dR9rAvYmadUfVdb'
    address2='AKnbvRwL1MSPFWoS6bdD5v2SNHq2uta5tm'
    print("------------------")
    resStr = dataGet(address1)
    resStr = dataGet(address2)
