#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "achuDk"
# Date: 2018/6/3


"""
步骤：
    1.获取尚未采集数据的主机列表
    2.采集并整理数据
    3.发送数据
"""

# 1.获取尚未采集数据的主机列表
import requests

# ret = requests.get('http://127.0.0.1:8080/asset.html')

ret = ['host2','host3']

# 2.采集并整理数据
import paramiko

# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_host文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
# 连接服务器
ssh.connect(hostname='192.168.0.124',port=22,username='root',password='123456')
# 执行命令
stdin,stdout,stderr = ssh.exec_command('yum install net-tools')
stdin.write(b'y')
stdin,stdout,stderr = ssh.exec_command('ifconfig')
# 获取命令结果
ret1 = stdout.read().decode()
ret2 = stderr.read().decode()
print(ret1,ret2)
# 关闭连接
ssh.close()

# 整理数据
info_dic = {
    'cpu':{},
    'mem':{},
    'nic':{},
    'disk':{},
}

# 3.发送数据至API
import requests

requests.post('http://127.0.0.1:8080/asset.html',data=info_dic)