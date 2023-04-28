#!/usr/bin/env python
import requests
import time
import random
import string
import hashlib
from string import Template
import json

count = 0
list = []

# 参数部分

url = "some url"

header = {
    'Connection': 'close',
    'Accept': 'application/json,image/gif, image/jpeg, image/pjpeg, image/pjpeg, application/x-shockwave-flash, */*',
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727)',
    "Content-Type": "application/json; charset=UTF-8",
    "Cookie": "some cookie"
}

somelist = [
    "xxx",
    "yyy",
    "zzz",
]

dataTemp = Template('{\
"ele": "${ele}",\
"random_str_8": "${random_str_8}",\
"timestamp": ${timestamp},\
"sha1_str": "${sha1_str}",\
"md5_str": "${md5_str}"}')

for ele in somelist:
    # 过滤 None
    if ele == None:
        print("{} is None: ", ele)
        continue

    # a-zA-Z0-9 随机字符串
    random_str_8 = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    # 时间戳
    timestamp = int(round(time.time() * 1000))
    # sha1
    sha1_str = hashlib.sha1(random_str_8.encode()).hexdigest()
    # md5
    md5_str = hashlib.md5(str(timestamp).encode()).hexdigest()

    params_str = dataTemp.substitute(ele=ele, random_str_8=random_str_8, timestamp=timestamp, sha1_str=sha1_str, md5_str=md5_str)

    print("requests params: \n", params_str)
    response = requests.post(url=url, headers=header, data=params_str)
    print("response: \n", response.json())

    count += 1
    # 获取响应状态码
    if (response.status_code == 200):
        list.append(count)
    else:
        print(response.status_code)
        print(response.content)
    print("这是第 {0} 次发送\n".format(count))

print("测试结束，下面是测试实效的序号：")
print(list)

# dict to json 字符串

# temp = {
#     "a": str("a"),
#     "b": "b",
#     "c": "b",
#     "d": "d",
#     "e": "e",
#     "f": {
#         "g": (int(round(time.time() * 1000)) - 15 * 24 * 60 * 60 * 1000),
#         "h": (int(round(time.time() * 1000))),
#     },
# }

# print("requests params: \n", json.dumps(temp))
# response = requests.post(url=url, headers=header, data=json.dumps(temp))