#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "achuDk"
# Date: 2018/6/3

# 将获取到的disk、mem、nic等信息进行打包

# 1. 初级版本
"""
from .plugins.Disk import DiskPlugin
from .plugins.Mem import MemPlugin
from .plugins.Nic import NicPlugin

def pack():
    disk = DiskPlugin()
    disk_info = disk.execute()

    mem = MemPlugin()
    mem_info = mem.execute()

    nic = NicPlugin()
    nic_info = nic.execute()

    response = {
        'disk':disk_info,
        'mem':mem_info,
        'nic':nic_info,
    }

    return response
"""

# 2. 改进版本

from conf import settings
import importlib

response = {}
def pack():
    # 根据配置文件，导入要加载的模块
    for k,v in settings.plugins.items():
        cls_name,m_path = v.rsplit('.',maxsplit=1)
        m = importlib.import_module(m_path)
        cls = getattr(m,cls_name)
        response[k] = cls().execute()
    return response