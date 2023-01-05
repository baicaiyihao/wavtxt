import json
import time

import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder


def upload_file_to_server(headers, file_path, file_name):
    try:
        global wavtxtList, wavtxtResult
        url = 'https://smart.lenovo.com.cn/audioservice/voice/wav2txt?language=cn&videoName=audio.mp3&videoSize=38254&period=4780'

        files = {
            'file': (file_name, open(file_path, 'rb'), 'audio/mpeg')
        }

        formatdate = MultipartEncoder(files)
        uploadHeaders = headers
        uploadHeaders['Content-Type'] = formatdate.content_type
        results = requests.request('POST', url=url, headers=uploadHeaders, data=formatdate)
        response = results.json()
        if response['status'] == 'Y':
            taskId = response['res']['taskId']
            check = False
            while check == False:
                time.sleep(2)
                if len(setWavtxt(headers)) != 0:
                    wavtxtList = setWavtxt(headers)
                    check = True
            wavtxtResult = getWavtxt(wavtxtList, taskId)
            delWavtxtResult(taskId, headers)
        else:
            print('上传失败')
        return wavtxtResult
    except Exception as e:
        print(e)


def setWavtxt(headers):
    url = 'https://smart.lenovo.com.cn/audioservice/voice/getUserTaskList?isFinish=1&pn=1&rn=10'
    results = requests.request('GET', url=url, headers=headers)
    response = results.json()
    return response['res']['rows']


def getWavtxt(response, taskId):
    wavtxtResults = response
    for i in wavtxtResults:
        wavtxtResultsStr = json.dumps(i)
        wavtxtResultsJson = json.loads(wavtxtResultsStr)
        cherkTaskId = wavtxtResultsJson['taskId']
        if taskId == str(cherkTaskId):
            txtResult = wavtxtResultsJson['asrTxt']
            a = eval(txtResult)
            b = json.dumps(a[0])
            c = json.loads(b)
            return c['onebest']
        else:
            print('未查询到结果')


def delWavtxtResult(taskId, headers):
    url = 'https://smart.lenovo.com.cn/audioservice/voice/deleteTask?taskId=' + taskId
    result = requests.request('GET', url=url, headers=headers)
    # if result.json()['status'] == 'Y':
    #     print('任务删除成功')
