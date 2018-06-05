#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "achuDk"
# Date: 2018/6/3

from conf import settings

# 插件式设计，实现可插拔式管理
class BasePlugin():
    def __init__(self):
        mode_list = ['Agent','SSH','Salt']
        if self.mode in mode_list:
            self.mode = settings.MODE
        else:
            raise Exception('配置文件模式错误')

    # 定义三种模式执行命令的方法
    def agent(self,cmd):
        pass

    def ssh(self,cmd):
        pass

    def salt(self,cmd):
        pass

    # 判断cmdb实现的模式
    def shell_cmd(self,cmd):
        if self.mode == 'Agent':
            ret = self.agent(cmd)
        elif self.mode == 'SSH':
            ret = self.ssh(cmd)
        elif self.mode == 'Salt':
            ret = self.salt(cmd)
        else:
            raise Exception('代码中模式错误')
        return ret

    # 判断主机的系统平台
    def execute(self):
        # 此处执行判断平台的命令
        ret = self.shell_cmd('判断平台命令')
        if ret == 'windows':
            return self.windows()
        elif ret == 'linux':
            return self.linux()
        else:
            raise Exception('只支持windows和linux平台.')

    def windows(self):
        raise Exception('未定义该方法')

    def linux(self):
        raise Exception('未定义该方法')