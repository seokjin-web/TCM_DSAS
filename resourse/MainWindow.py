#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/11/25 0025 19:54
#@Author  :    tb_youth
#@FileName:    MainWindow.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
主界面
'''

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox
from PyQt5.QtWidgets import QListWidget,QListWidgetItem,QStackedWidget
from PyQt5.QtWidgets import QHBoxLayout,QStyleFactory
from PyQt5.QtGui import QIcon,QPixmap,QPalette,QBrush

from resourse import InputWindow as IW
from resourse import SelectionWindow as SW
from resourse import DataCenterWindow
from resourse import ContactWindow
from resourse import AboutUSWindow

class MainWindowDemo(QWidget):
    def __init__(self):
        super(MainWindowDemo,self).__init__()
        self.initUI()
        QApplication.setStyle(QStyleFactory.keys()[2])

    def initUI(self):
        self.setGeometry(450,100,1000,800)
        self.setWindowTitle('中医药数据特征选择分析平台')

        self.list_widget = QListWidget()
        self.item_list = ['平台首页','数据导入','特征选择','数据中心','算法中心','知识中心','反馈建议','关于我们']
        self.list_widget.addItems(self.item_list)
        item1 = QListWidgetItem()
        self.list_widget.addItem(item1)
        # quit = QLabel('退出')
        # quit.setPixmap(QPixmap('./image/退出.png'))

        # quit = QPushButton('退出')
        # quit.setMaximumSize(80, 50)
        # quit.setIcon(QIcon(QPixmap('./image/退出.png')))
        # quit.clicked.connect(self.close)

        # sizePolicy = QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed)
        # # print(quit.size())
        # quit.setSizePolicy(sizePolicy)
        # self.list_widget.setItemWidget(item1,quit)

        #设置item间隔
        self.list_widget.setSpacing(5)

        #创建各个功能子窗口
        self.interface_widget = IntefaceWindow()
        self.input_widget = IW.InputWindowDemo()
        self.select_feature_widget = SW.SelectionWindowdemo()
        # self.analyze_data_widget = QWidget()
        self.database_widget = DataCenterWindow.DataCenterWindow()
        self.algorithm_widget = QWidget()
        self.konwledge_widget = QWidget()
        self.contact_widget = ContactWindow.ConcatWindow()
        self.about_widget = AboutUSWindow.AboutUSWindowDemo()

        #将各个功能子窗口压入栈窗口
        self.stack_widget = QStackedWidget()
        self.stack_widget.addWidget(self.interface_widget)
        self.stack_widget.addWidget(self.input_widget)
        self.stack_widget.addWidget(self.select_feature_widget)
        # self.stack_widget.addWidget(self.analyze_data_widget)
        self.stack_widget.addWidget(self.database_widget)
        self.stack_widget.addWidget(self.algorithm_widget)
        self.stack_widget.addWidget(self.konwledge_widget)
        self.stack_widget.addWidget(self.contact_widget)
        self.stack_widget.addWidget(self.about_widget)

        #布局
        hlayout = QHBoxLayout()
        hlayout.addWidget(self.list_widget)
        hlayout.addWidget(self.stack_widget)
        #等比例划分布局
        hlayout.setStretch(0,1)
        hlayout.setStretch(1,5)
        self.setLayout(hlayout)

        #美化:
        #去边框
        self.list_widget.setFrameShape(False)
        #icon
        self.setWindowIcon(QIcon('../image/分析.png'))
        # 背景图片
        # palette = QPalette()
        # pix = QPixmap(r'./')
        # pix.scaled(self.width(),self.height())
        # palette.setBrush(QPalette.Background,QBrush(pix))
        # self.setPalette(palette)

        #关联单击信号
        self.list_widget.currentRowChanged.connect(self.onClickedListWidget)
        #导入数据窗口与特征选择窗口信号与槽关联，用于传递导入的数据

    #根据index切换功能子窗口
    def onClickedListWidget(self,index):
        print(index)
        if index == 2:
            data = self.input_widget.tab1.data
            var_list = self.input_widget.tab1.var_list
            try:
                self.select_feature_widget.data = data
                self.select_feature_widget.var_list = var_list
            except:
                pass
        self.stack_widget.setCurrentIndex(index)








class IntefaceWindow(QWidget):
    def __init__(self):
        super(IntefaceWindow,self).__init__()
        # 背景图片
        palette = QPalette()
        pix = QPixmap(r'../image/1.png')
        pix.scaled(self.width(),self.height())
        palette.setBrush(QPalette.Background,QBrush(pix))
        self.setPalette(palette)




if __name__=='__main__':
    app = QApplication(sys.argv)
    window = MainWindowDemo()
    window.show()
    sys.exit(app.exec_())