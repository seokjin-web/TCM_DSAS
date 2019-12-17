#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/12/14 0014 22:31
#@Author  :    tb_youth
#@FileName:    Morse.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth


class MorseDemo(object):
    key_list1 = ['01', '1000', '1010', '100', '0', '0010',
                '110', '0000', '00', '0111', '101', '0100',
                '11', '10', '111', '0110', '1101', '010',
                '000', '1', '001', '0001', '011', '1001',
                '1011', '1100', '01111', '00111', '00011',
                '00001', '00000', '10000', '11000', '11100',
                '11110', '11111', '001100', '10010', '101101',
                '100001', '010101', '110011', '011010', '111000',
                '101010', '10001', '011110', '101011', '001101',
                '010010', '10110', '1111011', '1111101']

    value_list = ['A', 'B', 'C', 'D', 'E','F', 'G',
                  'H', 'I', 'J', 'K', 'L', 'M', 'N',
                  'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                  'W', 'X', 'Y', 'Z', '1', '2', '3', '4',
                  '5', '6', '7', '8', '9', '0', '?', '/',
                  '()', '-', '.', ',', '@', ':', ':',
                  '=', "'", '!', '_', '"', '(', '{', '}']

    def __init__(self):
        self.key_list2 = [item.replace('0','.').replace('1','-') for item in self.key_list1]
        self.encode_dict = dict(zip(self.value_list,self.key_list2))
        self.decode_dict = dict(zip(self.key_list2,self.value_list))

    def decode(self,string):
        word_list = string.split()
        res1 = ''.join([self.decode_dict.get(word.strip()) for word in word_list])
        res2 = res1.lower()
        return res1,res2

    def encode(self,string):
        res1 = ' '.join([self.encode_dict.get(item) for item in string])
        res2 = res1.replace('.','0').replace('-','1')
        return res1,res2
