#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/12/15 0015 1:20
#@Author  :    tb_youth
#@FileName:    DataCenterWindow.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

import sys
from PyQt5.QtWidgets import QWidget,QApplication,QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class DataCenterWindow(QWidget):
    def __init__(self):
        super(DataCenterWindow,self).__init__()
        self.initUI()

    def initUI(self):
        self.browser = QWebEngineView()
        self.url = QUrl(r"https://archive.ics.uci.edu/ml/index.php")
        self.browser.load(self.url)
        vlayout = QVBoxLayout()
        vlayout.addWidget(self.browser)
        self.setLayout(vlayout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DataCenterWindow()
    window.show()
    sys.exit(app.exec_())