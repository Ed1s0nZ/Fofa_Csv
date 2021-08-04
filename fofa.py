# -*- coding: utf-8 -*-
import base64
import time
import requests
import sys
import io
import csv


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')  # 改变标准输出的默认编码 encoding='gb18030'


def search(qbase64):
    url = "https://fofa.so/api/v1/search/all/"
    params = {

        'email': email,
        'key': key,
        'qbase64': qbase64
    }
    r = requests.get(url, params=params)
    res = r.json()
    print(res)
    size = res['size']
    print(size)
    for i in range(1, size // 1000 + 2):
        params = {
            'email': email,
            'key': key,
            'qbase64': qbase64,
            'page': i,
            'size': search_size,
            'fields': 'ip,port,host,title,server'
        }
        r = requests.get(url, params=params)
        res = r.json()
        result = res['results']
        print(result)
        # 获取domain和title
        with open(name+'.csv', 'a', newline='', encoding="gb18030") as f:
            for r in result:
                assets_all.append([r[0] + ':' + r[1], r[2], r[3], r[4]])
            f_csv = csv.writer(f)
            f_csv.writerows(assets_all)
    time.sleep(30)


if __name__ == "__main__":
    email = "*******************"
    key = "*****************************"
    search_size = "10000"  # 高级会员10000条
    name = "jiangnan"
    assets_all = []
    with open(name + '.txt', 'r', encoding='utf-8') as f:  # encoding='utf-8'
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        qbase64 = base64.b64encode(line.encode())
        search(qbase64)
