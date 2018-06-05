#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "achuDk"
# Date: 2018/6/3

from .Base import BasePlugin

class MemPlugin(BasePlugin):
    def linux(self):
        ret = self.shell_cmd('free -m')
        return ret
    def windows(self):
        ret = self.shell_cmd('不知道')
        return ret