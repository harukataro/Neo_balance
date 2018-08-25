# -*- coding: utf-8 -*-

import requests
import json


def dataGet(address):


    # neoscan
    url = 'https://neoscan.io/'
    targetBlock = 2640000

    #APIextention
    NeoGetBalance='api/main_net/v1/get_balance/'
    NeoGetTran='api/main_net/v1/get_address_abstracts/'

    # urlの作成
    paramStrB = url+NeoGetBalance+address
    paramStrT = url+NeoGetTran+address+'/1'

    response= requests.get(paramStrB)
    content = response.json()

    #特定のキーの残高の抽出
    for key in content['balance']:
        if key['asset'] == "NEO":
                    Balance = key['amount']


    response=requests.get(paramStrT)
    content = response.json()

    for key in content['entries']:
            #print(key['block_height'],key['amount'],key['address_to'])
            if key['block_height'] > targetBlock:
                if key['address_to'] == address:
                    amount = float(key['amount'])
                    Balance = Balance + amount
                    #print(Balance)
                else:
                    Balance = Balance - amount
                    #print(Balance)
    return Balance

if __name__ == '__main__':

    #NEO Address
    address1='AXDt2hzT35knLnV3MB3dR9rAvYmadUfVdb'
    address2='AKnbvRwL1MSPFWoS6bdD5v2SNHq2uta5tm'
    print("==================")
    resStr = dataGet(address1)
    print("NEO address: ",address1)
    print("Balances: ",resStr)
    print("==================")
    resStr = dataGet(address2)
    print("NEO address: ",address2)
    print("Balances: ",resStr)
    print("==================")
