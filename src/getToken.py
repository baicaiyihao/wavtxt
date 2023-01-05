import time
import requests
import json


def getTimestamp():
    Timestamp = int(time.time()*1000)
    cookie = 'avt_v=vid=>1850ffce73b1102|||fsts=>' + str(Timestamp) +'|||dsfs=>20920|||nps=>2; avt_s=lsts=>' + str(Timestamp) +'|||sid=>0252890787|||vs=>2|||source=>direct|||pref=>https://lva.lenovo.com.cn/|||ref=>'
    return cookie


def getTokencui():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
        'Content-Type': 'application/json'
    }

    body = {"lenovo_id_info": {"realm": "api.iot.lenovomm.com", "ticket": ""}, "client_key": "60a3327c94df8b95f0ccb7a4",
            "device_info": {"device_id": "d0efd8b7-1289-4b70-b607-edaaf7b11a77", "mac": "", "vendor": "UNKNOW_TYPE",
                            "hw_model": "Chrome_Text_Translation", "client_sw_ver": "2.0.0"},
            "product_id": "Chrome_Text_Translation"}
    data = json.dumps(body)
    url = 'https://cuiauth.lenovo.com.cn/auth/v1/simpletoken'

    r = requests.post(url, data=data, headers=headers)
    response = r.json()
    Tokencui = response['data']['access_token']
    return Tokencui
