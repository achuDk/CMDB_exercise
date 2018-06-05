#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "achuDk"
# Date: 2018/6/3


"""
步骤：
    1.安装SaltStack
    2.获取未采集信息的主机列表
    3.通过SaltStack的master采集数据并整理
    4.将数据发送至CMDB的API
"""

# 1.安装SaltStack
# 在所有主机上执行命令
"""
    yum install https://repo.saltstack.com/yum/redhat/salt-repo-latest-2.el6.noarch.rpm
    yun clean all
"""
# 准备工作
    # 在master上执行
"""
        yum install salt-master
        # 初始化配置文件
        vim /etc/salt/master
            interface: 192.168.0.124
        service salt-master status
        # 启动saltstack服务
        service salt-master start
"""
    # 在minion上执行
"""
        yum install salt-minion
        # 初始化配置文件
        vim /etc/salt/minion
            master: 192.168.0.124
        service salt-master status
        # 启动saltstack服务
        service salt-minion status
        service salt-minion start
"""

# 主从连接
    # 在master  查看所有minion
"""
        [root@host1 ~]# salt-key -L
        Accepted Keys:
        Denied Keys:
        Unaccepted Keys:
        host2
        host3
        Rejected Keys:
"""
    # 在master上添加minion
"""
        [root@host1 ~]# salt-key -a host2
        The following keys are going to be accepted:
        Unaccepted Keys:
        host2
        Proceed? [n/Y] Y
        Key for minion host2 accepted.
"""

# 远程执行命令
"""
        [root@host1 ~]# salt 'host2' cmd.run 'hostname'
        host2:
            host2
            
    # 在所有minion上执行命令：
        
        [root@host1 ~]# salt '*' cmd.run 'hostname'
        host2:
            host2
        host3:
            host3
    """
# 通过python代码来实现远程执行命令
    # 在master上执行
"""
        [root@host1 ~]# /usr/bin/python2.7
        >>> import salt
        >>> from salt import client
        >>> local=salt.client.LocalClient()
        >>> result = local.cmd('host2','cmd.run',['hostname'])
        >>> type(result)
        <type 'dict'>
        >>> result
        {u'host2': u'host2'}
        >>> result.keys()
        [u'host2']
        >>> result.values()
        [u'host2']
        >>> exit()
"""

# 2.获取未采集信息的主机列表
import requests

# ret = requests.get('http://127.0.0.1:8080/asset.html')

ret = ['host2','host3']

# 3.采集数据——通过远程服务器执行命令
# 在saltstack的master的主机上执行python代码

"""
import salt
from salt import client
local=salt.client.LocalClient()
result = local.cmd('host2','cmd.run',['hostname'])
"""

# 整理数据
info_dic = {
    'cpu':{},
    'mem':{},
    'nic':{},
    'disk':{},
}

# 4.发送数据至API
import requests

requests.post('http://127.0.0.1:8080/asset.html',data=info_dic)