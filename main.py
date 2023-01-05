import os

import getWavtxt,getToken

def main():
    global inputFile
    Cookie = getToken.getTimestamp()
    Tokencui = getToken.getTokencui()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
        'Cookie': Cookie,
        'Tokencui': Tokencui
    }
    while True:
        file = input(f'请输入文件路径 或 直接拖入：')
        if file == '':
            continue
        if os.path.exists(file.strip('\'"')):
            inputFile = file.strip('\'"')
            break
        else:
            print('输入的文件不存在，请重新输入')
    #建议写入绝对物理路径
    file_path = inputFile
    file_name = os.path.split(file_path)[-1]
    txt = getWavtxt.upload_file_to_server(headers, file_path, file_name)
    print('文件内容为：'+txt)

if __name__ == '__main__':
    main()