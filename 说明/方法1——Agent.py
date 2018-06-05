#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "achuDk"
# Date: 2018/6/3

"""
步骤：
    1.采集并整理数据
    2.发送数据

"""


import subprocess

# 1.采集数据
ret = subprocess.getoutput('ipconfig')
print(ret)

# 整理数据
info_dic = {
    'cpu':{},
    'mem':{},
    'nic':{},
    'disk':{},
}

# 2.发送数据至API
import requests

requests.post('http://127.0.0.1:8080/asset.html',data=info_dic)