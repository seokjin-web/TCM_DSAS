#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    15:17  2019/12/13
#@Author  :    tb_youth
#@FileName:    DataFrameListMTF.py
#@SoftWare:    PyCharm
#@Blog    :    http://blog.csdn.net/tb_youth

'''
DataFrame 和 list 相互转换,
包括DataFrame的index与columns，
DataFrameListMutualTransform: DataFrameListMTF
'''
import pandas as pd

class DataFrameListMTF():
    def __init__(self):
        pass

    def list_to_DataFrame(self,lst):
        df = pd.DataFrame(lst)
        index_list = list(df.iloc[1:, 0])
        column_list = list(df.iloc[0, 1:])
        data = df.iloc[1:, 1:]
        data.index = index_list
        data.columns = column_list
        return data

    def DataFrame_to_list(self,df):
        data_list = [[''] + df.columns.values.tolist()]
        index_list = df.index.values.tolist()
        for i, item in enumerate(df.values.tolist()):
            data_list.append([index_list[i]] + item)
        return data_list


if __name__=='__main__':
    pass
