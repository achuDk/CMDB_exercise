#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "achuDk"
# Date: 2018/6/3


# 定义程序运行模式
MODE = 'Agent'
# MODE = 'SSH'
# MODE = 'Salt'

# 定义要加载的插件，不需要的可以注释掉
plugins = {
    'disk' : 'src.plugins.Disk.DiskPlugin',
    'mem' : 'src.plugins.Mem.MemPlugin',
    'nic' : 'src.plugins.Nic.NicPlugin',
    # 'cpu' : 'src.plugins.Cpu.Cpuplugin',
}