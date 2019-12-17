#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/12/14 0014 23:04
#@Author  :    tb_youth
#@FileName:    AboutUSWindow.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
显示本项目的一些信息,
跳转到github仓库。
'''
import sys
import webbrowser
from PyQt5.QtWidgets import QApplication,QWidget,QTextBrowser
from PyQt5.QtWidgets import QVBoxLayout,QHBoxLayout,QPushButton
from PyQt5.QtGui import QIcon,QPixmap
from resourse import LoadQSSHelper
# import os

class AboutUSWindowDemo(QWidget):
    def __init__(self):
        super(AboutUSWindowDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(800,800)
        self.setWindowTitle('关于我们')
        icon = QIcon()
        #切换到上一目录，便于使用其他资源
        # os.chdir('..')
        # print(os.getcwd())
        icon.addPixmap(QPixmap('../image/school_logo_nobg.png'),QIcon.Normal,QIcon.Off)
        self.setWindowIcon(icon)
        self.text_brower = QTextBrowser()
        with open('../about','r',encoding='utf-8') as f:
            text = f.read()
        self.text_brower.setPlainText(text)
        self.button = QPushButton('前往GitHub给我们Star')
        self.button.setIcon(QIcon('../image/star.png'))
        qss_file = '../qss_/aboutWindowStyle.qss'
        load_help = LoadQSSHelper.LoadQSSHelper()
        style = load_help.load(qss_file)
        self.button.setStyleSheet(style)
        vlayout = QVBoxLayout()
        vlayout.addWidget(self.text_brower)
        vlayout.addWidget(self.button)
        self.setLayout(vlayout)
        self.button.clicked.connect(self.onClickedOpen)


    def onClickedOpen(self):
        url = r'https://github.com/tbyouth/Learn-python-notes/tree/master/projects/demo/Work/TCM_DSAS'
        webbrowser.open(url)





if __name__=='__main__':
    app = QApplication(sys.argv)
    window = AboutUSWindowDemo()
    window.show()
    sys.exit(app.exec_())

