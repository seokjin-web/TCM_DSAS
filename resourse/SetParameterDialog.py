#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/11/27 0027 19:25
#@Author  :    tb_youth
#@FileName:    SetParameterDialog.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
此界面用于设置特征选择所需设置的相关参数
'''

import sys
from PyQt5.QtWidgets import QApplication,QDialog,QLabel,QLineEdit
from PyQt5.QtWidgets import QFormLayout,QHBoxLayout,QPushButton
from PyQt5.QtGui import QIntValidator,QIcon
from PyQt5.QtCore import pyqtSignal,pyqtSlot,QObject


#自定义的信号类，用于窗口通信
class MySignal(QObject):
    sender = pyqtSignal(dict)
    def send(self,parameter_dict):
        self.sender.emit(parameter_dict)

#FSFS
class ParamerterDemo(QDialog):
    def __init__(self):
        super(ParamerterDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(400,200)
        self.setMaximumSize(400,200)
        self.setWindowTitle('设置参数')
        self.setWindowIcon(QIcon('../image/参数.png'))
        self.signal = MySignal()
        self.defuat_parameter_list = [100, 3, 10, 10, 5]

        self.form_layout = QFormLayout()

        self.lable1 = QLabel()
        self.lable1.setText('特征得分Top:')
        self.lable1.setToolTip('过滤过程')
        self.line_edit1 = QLineEdit()
        self.line_edit1.setValidator(QIntValidator())
        self.line_edit1.setText('100')
        self.form_layout.addRow(self.lable1, self.line_edit1)

        self.lable2 = QLabel()
        self.lable2.setText('主成分个数:')
        self.lable2.setToolTip('PLS中的主成分分析')
        self.line_edit2 = QLineEdit()
        self.line_edit2.setValidator(QIntValidator())
        self.line_edit2.setText('3')
        self.form_layout.addRow(self.lable2,self.line_edit2)

        self.lable3 = QLabel()
        self.lable3.setText('K折交叉验证:')
        self.lable3.setToolTip('K折交叉验证')
        self.line_edit3 = QLineEdit()
        self.line_edit3.setValidator(QIntValidator())
        self.line_edit3.setText('10')
        self.form_layout.addRow(self.lable3, self.line_edit3)

        self.lable4 = QLabel()
        self.lable4.setText('Wrapper步长:')
        self.lable4.setToolTip('封装过程')
        self.line_edit4 = QLineEdit()
        self.line_edit4.setPlaceholderText('步长最好要能被特征总数整除')
        self.line_edit4.setValidator(QIntValidator())
        self.line_edit4.setText('10')
        self.form_layout.addRow(self.lable4, self.line_edit4)

        self.lable5 = QLabel()
        self.lable5.setText('频次阈值alp:')
        self.lable5.setToolTip('投票过程')
        self.line_edit5 = QLineEdit()
        self.line_edit5.setPlaceholderText('使用的是多数投票法')
        self.line_edit5.setValidator(QIntValidator())
        self.line_edit5.setText('5')
        self.form_layout.addRow(self.lable5, self.line_edit5)

        self.button1 = QPushButton('重置')
        self.button1.setToolTip('重置为默认值')
        self.button2 = QPushButton('取消')
        self.button2.setToolTip('退出设置参数')
        self.button3 = QPushButton('完成')
        self.button3.setToolTip('确认设置参数')
        hlayout = QHBoxLayout()
        hlayout.addWidget(self.button1)
        hlayout.addWidget(self.button2)
        hlayout.addWidget(self.button3)
        hlayout.setSpacing(20)
        self.form_layout.addItem(hlayout)
        self.setLayout(self.form_layout)

        #关联信号
        self.button1.clicked.connect(self.reSetParameter)
        self.button2.clicked.connect(self.close)
        self.button3.clicked.connect(self.sendSignal)

    #重置参数
    def reSetParameter(self):
        for i in range(1,6):
            try:
                command = 'self.line_edit{}.setText(str(self.defuat_parameter_list[i-1]))'.format(i)
                eval(command)
            except Exception as e:
                print(e)
                pass

    #参数设置完成，发送信号并关闭设置参数对话框
    def sendSignal(self):
        parameter_dict = {
            'topK': int(self.line_edit1.text()),
            'n_components': int(self.line_edit2.text()),
            'K': int(self.line_edit3.text()),
            'step': int(self.line_edit4.text()),
            'alp': int(self.line_edit5.text()),
        }
        self.signal.send(parameter_dict)
        self.close()


#Lasso
class ParamerterDemo2(QDialog):
    def __init__(self):
        super(ParamerterDemo2,self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(400,200)
        self.setMaximumSize(400,200)
        self.setWindowTitle('设置参数')
        self.setWindowIcon(QIcon('../image/参数.png'))
        self.signal = MySignal()
        self.defuat_parameter_list = [50,20000]

        self.form_layout = QFormLayout()

        self.lable1 = QLabel()
        self.lable1.setText('alpha:')
        self.lable1.setToolTip('alpha')
        self.line_edit1 = QLineEdit()
        self.line_edit1.setValidator(QIntValidator())
        self.line_edit1.setText('50')
        self.form_layout.addRow(self.lable1, self.line_edit1)

        self.lable2 = QLabel()
        self.lable2.setText('max_iter:')
        self.lable2.setToolTip('最大迭代次数')
        self.line_edit2 = QLineEdit()
        self.line_edit2.setValidator(QIntValidator())
        self.line_edit2.setText('20000')
        self.form_layout.addRow(self.lable2,self.line_edit2)

        self.button1 = QPushButton('重置')
        self.button1.setToolTip('重置为默认值')
        self.button2 = QPushButton('取消')
        self.button2.setToolTip('退出设置参数')
        self.button3 = QPushButton('完成')
        self.button3.setToolTip('确认设置参数')
        hlayout = QHBoxLayout()
        hlayout.addWidget(self.button1)
        hlayout.addWidget(self.button2)
        hlayout.addWidget(self.button3)
        hlayout.setSpacing(20)
        self.form_layout.addItem(hlayout)
        self.setLayout(self.form_layout)

        #关联信号
        self.button1.clicked.connect(self.reSetParameter)
        self.button2.clicked.connect(self.close)
        self.button3.clicked.connect(self.sendSignal)

    #重置参数
    def reSetParameter(self):
        for i in range(1,3):
            try:
                command = 'self.line_edit{}.setText(str(self.defuat_parameter_list[i-1]))'.format(i)
                eval(command)
            except Exception as e:
                print(e)
                pass

    #参数设置完成，发送信号并关闭设置参数对话框
    def sendSignal(self):
        parameter_dict = {
            'alpha': int(self.line_edit1.text()),
            'max_iter': int(self.line_edit2.text()),
        }
        self.signal.send(parameter_dict)
        self.close()


if __name__=='__main__':
    app = QApplication(sys.argv)
    window = ParamerterDemo()
    window.show()
    sys.exit(app.exec_())