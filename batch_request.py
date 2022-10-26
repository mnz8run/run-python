#!/usr/bin/env python
import requests
import json
from string import Template

url = "some url"

header = {
    'Connection': 'close',
    'Accept': 'application/json,image/gif, image/jpeg, image/pjpeg, image/pjpeg, application/x-shockwave-flash, */*',
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727)',
    "Content-Type": "application/json; charset=UTF-8",
    "Cookie": "some cookie"
}

f = open('some.json')
someDict = json.load(f)
count = 0
list = []

dataTemp = Template('{"someKey": "${key}", "someValue": [${value}]}')
"""
body='{"xxx":"yyy"}'

response=requests.post(url=url,headers=header,data=body)
print(response)
"""

for key, value in someDict.items():
    # 过滤 None
    if value == None:
        print("NoneKey: ", key)
        continue

    response = requests.post(url=url, headers=header, data=dataTemp.substitute(key=key, value=value))
    count += 1
    # 获取响应状态码
    if (response.status_code == 200):
        list.append(count)
    else:
        print(response.status_code)  # 状态码
        print(response.content)  # 响应内容
    print("这是第：{0} 次发送".format(count))

print("测试结束，下面是测试实效的序号：")
print(list)

f.close()