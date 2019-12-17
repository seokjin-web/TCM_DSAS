#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    14:44  2019/12/16
#@Author  :    tb_youth
#@FileName:    VariableSettingWindow.py
#@SoftWare:    PyCharm
#@Blog    :    http://blog.csdn.net/tb_youth


import sys
from PyQt5.QtWidgets import QApplication,QDialog,QAbstractItemView
from PyQt5.QtWidgets import QListWidget,QLabel,QPushButton
from PyQt5.QtWidgets import QVBoxLayout,QHBoxLayout,QGridLayout
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtCore import QObject,pyqtSignal

class MySignal(QObject):
    sender = pyqtSignal(list)
    def send(self,var_list):
        self.sender.emit(var_list)

class VariableSettingWindowDemo(QDialog):
    def __init__(self,data_list):
        super(VariableSettingWindowDemo,self).__init__()
        self.initUI(data_list)
        
    
    def initUI(self,data_list):
        self.resize(800,800)
        self.setWindowTitle('变量设置')
        self.signal = MySignal()
        icon = QIcon()
        icon.addPixmap(QPixmap('../image/设置.png'))
        self.setWindowIcon(icon)
        self.label1 = QLabel('变量')
        self.label2 = QLabel('自变量')
        self.label3 = QLabel('因变量')
        
        self.list_widget1 = QListWidget()
        self.list_widget2 = QListWidget()
        self.list_widget3 = QListWidget()

        self.list_widget1.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.list_widget2.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.list_widget3.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.list_widget1.addItems(data_list)
        
        self.button12 = QPushButton('-->')
        self.button21 = QPushButton('<--')

        self.button13 = QPushButton('-->')
        self.button31 = QPushButton('<--')

        self.button1 = QPushButton('确认')
        self.button2 = QPushButton('取消')
       
        
        vlayout1 = QVBoxLayout()
        vlayout1.addWidget(self.button12)
        vlayout1.addWidget(self.button21)
        
        hlayout1 = QHBoxLayout()
        hlayout1.addItem(vlayout1)
        vlayout = QVBoxLayout()
        # vlayout.addWidget(QLabel(''))
        vlayout.addWidget(self.label2)
        vlayout.addWidget(self.list_widget2)
        vlayout.setSpacing(10)
        hlayout1.addItem(vlayout)

        vlayout2 = QVBoxLayout()
        vlayout2.addWidget(self.button13)
        vlayout2.addWidget(self.button31)

        hlayout2 = QHBoxLayout()
        hlayout2.addItem(vlayout2)
        vlayout = QVBoxLayout()
        # vlayout.addWidget(QLabel(''))
        vlayout.addWidget(self.label3)
        vlayout.addWidget(self.list_widget3)
        vlayout.setSpacing(10)
        hlayout2.addItem(vlayout)

        gridlayout = QGridLayout()
        hlayout = QHBoxLayout()
        # hlayout.addWidget(self.button1)
        # hlayout.addWidget(self.button2)
        hlayout.setSpacing(20)

        vlayout = QVBoxLayout()
        vlayout.addItem(hlayout)
        vlayout.addWidget(self.label1)
        vlayout.addWidget(self.list_widget1)
        vlayout.setSpacing(10)


        gridlayout.addItem(vlayout,1,0,2,1)
        hlayout1.setSpacing(10)
        hlayout2.setSpacing(10)
        gridlayout.addItem(hlayout1,1,1,1,1)
        gridlayout.addItem(hlayout2,2,1,1,1)
        hlayout = QHBoxLayout()
        hlayout.addWidget(self.button1)
        hlayout.addWidget(self.button2)
        hlayout.setSpacing(10)
        gridlayout.addItem(hlayout,3,0,1,1)
        self.setLayout(gridlayout)


        #绑定信号
        self.button12.clicked.connect(lambda :self.onClickButton(self.list_widget1,self.list_widget2))
        self.button21.clicked.connect(lambda :self.onClickButton(self.list_widget2,self.list_widget1))
        self.button13.clicked.connect(lambda :self.onClickButton(self.list_widget1,self.list_widget3))
        self.button31.clicked.connect(lambda :self.onClickButton(self.list_widget3,self.list_widget1))
        self.button1.clicked.connect(self.sendSignal)
        self.button2.clicked.connect(self.close)

    def onClickButton(self,sender,reciever):
        try:
            item_list = sender.selectedItems()
            for item in item_list:
                reciever.addItem(item.text())
                sender.takeItem(sender.row(item))
        except Exception as e:
            print(e)

    def sendSignal(self):
        count1 = self.list_widget2.count()
        count2 = self.list_widget3.count()
        independ_var = [self.list_widget2.item(i).text() for i in range(count1)]
        depend_var = [self.list_widget3.item(i).text() for i in range(count2)]
        var_list = [independ_var, depend_var]
        self.signal.send(var_list)
        self.close()


  
  
if __name__=='__main__':
    app = QApplication(sys.argv)
    data_list = ['1','2','3','4','5']
    window = VariableSettingWindowDemo(data_list)
    window.show()
    sys.exit(app.exec_())