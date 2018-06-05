#! /usr/bin/env python
# -*- coding: utf-8 -*-

#

from .plugins import pack


class Baseclient():
    def send_data(self,data_dict):
        pass

class SBaseclient(Baseclient):
    def get_host_list(self):
        host_list = {}
        return host_list

class Agent(Baseclient):
    def process(self):
        data_dict = pack()
        self.send_data(data_dict)

class SSH(SBaseclient):
    def process(self):
        host_list = self.get_host_list()
        for host in host_list:
            data_dict = pack()
            self.send_data(data_dict)

class Salt(SBaseclient):
    def process(self):
        host_list = self.get_host_list()
        for host in host_list:
            data_dict = pack()
            self.send_data(data_dict)


from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import time
def test(i):
    time.sleep(1)
    print(i)

pool = ThreadPoolExecutor(3)
for i in range(1,22):
    pool.submit(test,i)
pool.shutdown()