#! /usr/bin/env python
# -*- coding: utf-8 -*-

from conf import settings
from . import client

def run():
    if settings.MODE == 'Agent':
        client.Agent().process()
    elif settings.MODE == 'SSH':
        client.SSH().process()
    elif settings.MODE == 'Salt':
        client.Salt().process()
    else:
        raise Exception('配置文件模式异常')