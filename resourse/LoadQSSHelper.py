#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/12/15 0015 1:09
#@Author  :    tb_youth
#@FileName:    LoadQSSHelper.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

class LoadQSSHelper():
    @staticmethod
    def load(qss_file):
        with open(qss_file, 'r', encoding='utf-8') as f:
            return f.read()


if __name__=='__main__':
    pass
