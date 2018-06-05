#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "achuDk"
# Date: 2018/6/3

from .Base import BasePlugin

class NicPlugin(BasePlugin):
    def linux(self):
        ret = self.shell_cmd('ifconfig')
        return ret
    def windows(self):
        ret = self.shell_cmd('ipconfig')
        return ret