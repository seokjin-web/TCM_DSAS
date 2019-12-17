#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/11/25 0025 22:41
#@Author  :    tb_youth
#@FileName:    InputWindow.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
导入数据界面：
支持数据预处理，数据查找
后期优化：动态加载数据，提升导入效率,设置加载数据进度条
'''

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QTabWidget
from PyQt5.QtWidgets import QTableView,QFileDialog,QPushButton
from PyQt5.QtWidgets import QMenuBar,QToolBar,QStatusBar,QAction,QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout,QSizePolicy,QLineEdit
from PyQt5.QtGui import QStandardItemModel,QPixmap,QIcon,QStandardItem,QColor
from PyQt5.QtCore import Qt,QDir
from openpyxl import workbook
import xlrd
import time

from resourse import VariableSettingWindow

#查找替换窗口
class  FindWidget(QWidget):
    def __init__(self):
        super(FindWidget,self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(80,800)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed)

        self.line_edit1 = QLineEdit()
        self.line_edit1.setPlaceholderText('find')
        self.line_edit2 = QLineEdit()
        self.line_edit2.setPlaceholderText('replace')

        self.tool_bar = QToolBar()
        self.search = QAction('查找')
        self.up = QAction('向上')
        self.down = QAction('向下')
        self.close = QAction('关闭')
        self.tool_bar.addAction(self.search)
        self.tool_bar.addAction(self.down)
        self.tool_bar.addAction(self.up)
        self.tool_bar.addAction(self.close)



        self.repalce_button = QPushButton('Replace')
        self.repalceAll_button = QPushButton('ReplaceAll')


        vlayout1 = QVBoxLayout()
        vlayout1.addWidget(self.line_edit1)
        vlayout1.addWidget(self.line_edit2)

        vlayout2 = QVBoxLayout()
        vlayout2.addWidget(self.tool_bar)

        hlayout1 = QHBoxLayout()
        hlayout1.addWidget(self.repalce_button)
        hlayout1.addWidget(self.repalceAll_button)
        vlayout2.addItem(hlayout1)

        layout = QHBoxLayout()
        layout.addItem(vlayout1)
        layout.addItem(vlayout2)
        self.setLayout(layout)

        self.close.triggered.connect(self.triggeredClose)
        icon = QIcon()
        icon.addPixmap(QPixmap('../image/查找.png'), QIcon.Normal, QIcon.Off)
        self.search.setIcon(icon)
        icon.addPixmap(QPixmap('../image/向下.png'), QIcon.Normal, QIcon.Off)
        self.down.setIcon(icon)
        icon.addPixmap(QPixmap('../image/向上.png'), QIcon.Normal, QIcon.Off)
        self.up.setIcon(icon)
        icon.addPixmap(QPixmap('../image/关闭.png'), QIcon.Normal, QIcon.Off)
        self.close.setIcon(icon)

    def triggeredClose(self):
        self.hide()



class WidgetDemo(QWidget):
    def __init__(self,mode):
        super(WidgetDemo,self).__init__()
        self.mode = mode
        self.initUI(mode)

    def initUI(self,mode):
        self.resize(800,800)
        #这里初始化，便于直接输入数据
        self.data = [['']*100 for i in range(15000)]
        self.res_pos = []
        self.focus_pos = None
        self.var_list = None
        #菜单栏
        self.menu = QMenuBar()
        self.file = self.menu.addMenu('文件')
        self.edit = self.menu.addMenu('编辑')
        self.view = self.menu.addMenu('视图')
        self.help = self.menu.addMenu('帮助')
        #各菜单下的子菜单

        #文件菜单下的子菜单
        self.new = self.file.addAction('新建')
        self.open = self.file.addAction('打开')
        self.save = self.file.addAction('保存')
        # self.save_as = self.file.addAction('另存为')


        #编辑菜单下的子菜单
        self.cut = self.edit.addAction('剪切')
        self.copy = self.edit.addAction('复制')
        self.paste = self.edit.addAction('粘贴')
        self.delete = self.edit.addAction('删除')
        self.find = self.edit.addAction('查找')
        self.replace = self.edit.addAction('替换')

        # 快捷键
        self.open.setShortcut('Ctrl+O')
        self.save.setShortcut('Ctrl+S')
        self.new.setShortcut('Ctrl+N')
        self.find.setShortcut('Ctrl+F')

        #视图菜单下的子菜单
        self.tool_view = QAction('工具栏',checkable=True)
        self.tool_view.setChecked(True)
        self.view.addAction(self.tool_view)

        self.statu_view = QAction('状态栏',checkable=True)
        self.statu_view.setChecked(True)
        self.view.addAction(self.statu_view)


        #帮助菜单下的子菜单
        self.about = self.help.addAction('关于')

        #工具栏
        self.tool_bar = QToolBar()
        self.tool_bar.addAction(self.new)
        self.tool_bar.addAction(self.open)
        self.tool_bar.addAction(self.save)
        self.tool_bar.addAction(self.cut)
        self.tool_bar.addAction(self.copy)
        self.tool_bar.addAction(self.paste)
        self.tool_bar.addAction(self.find)
        self.setting = QAction('变量设置')
        self.setting.setEnabled(False)
        self.tool_bar.addAction(self.setting)
        # self.tool_bar.addAction(self.replace)

        # #tool文本显示在下方
        # self.tool_bar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        #findWidge
        self.find_widget = FindWidget()
        self.find_widget.hide()

        #表格
        self.table_view = QTableView()
        self.table_view.setModel(self.mode)

        #状态栏
        self.status_bar = QStatusBar()
        self.status_bar.showMessage('这是一个状态栏')


        #创建布局
        layout = QVBoxLayout()
        layout.addWidget(self.menu)
        layout.addWidget(self.tool_bar)
        layout.addWidget(self.find_widget)
        layout.addWidget(self.table_view)
        layout.addWidget(self.status_bar)
        self.setLayout(layout)

        #关联信号
        self.open.triggered.connect(self.triggeredOpen)
        self.save.triggered.connect(self.triggeredSave)
        self.mode.itemChanged.connect(self.dealItemChanged)
        self.tool_view.triggered.connect(self.triggeredView)
        self.statu_view.triggered.connect(self.triggeredView)
        self.new.triggered.connect(self.triggeredNew)
        self.find.triggered.connect(self.triggeredFind)
        self.find_widget.search.triggered.connect(self.dataLocation)
        self.find_widget.down.triggered.connect(self.downLocation)
        self.find_widget.up.triggered.connect(self.upLocation)
        self.find_widget.close.triggered.connect(self.triggeredHideFind)
        self.find_widget.repalce_button.clicked.connect(self.onClickReplace)
        self.find_widget.repalceAll_button.clicked.connect(self.onClickReplaceAll)
        self.setting.triggered.connect(self.triggeredSetting)


        #美化
        icon = QIcon()
        icon.addPixmap(QPixmap('../image/打开.png'), QIcon.Normal, QIcon.Off)
        self.open.setIcon(icon)
        icon.addPixmap(QPixmap('../image/保存.png'), QIcon.Normal, QIcon.Off)
        self.save.setIcon(icon)
        icon.addPixmap(QPixmap('../image/新建.png'), QIcon.Normal, QIcon.Off)
        self.new.setIcon(icon)
        icon.addPixmap(QPixmap('../image/剪切.png'), QIcon.Normal, QIcon.Off)
        self.cut.setIcon(icon)
        icon.addPixmap(QPixmap('../image/复制.png'), QIcon.Normal, QIcon.Off)
        self.copy.setIcon(icon)
        icon.addPixmap(QPixmap('../image/粘贴.png'), QIcon.Normal, QIcon.Off)
        self.paste.setIcon(icon)
        icon.addPixmap(QPixmap('../image/查找1.png'), QIcon.Normal, QIcon.Off)
        self.find.setIcon(icon)
        icon.addPixmap(QPixmap('../image/设置.png'), QIcon.Normal, QIcon.Off)
        self.setting.setIcon(icon)
        # icon.addPixmap(QPixmap('../image/替换.png'), QIcon.Normal, QIcon.Off)
        # self.replace.setIcon(icon)



    def triggeredOpen(self):
        self.status_bar.showMessage('打开文件',5000)
        self.dialog = QFileDialog()
        self.dialog.setFileMode(QFileDialog.AnyFile)
        dir = r'../data'
        self.dialog.setDirectory(dir)
        self.dialog.setFilter(QDir.Files)
        if self.dialog.exec_():
            try:
                start = time.time()
                file_name = self.dialog.selectedFiles()[0]
                #这里读取数据返回列表便于表格中数据的更新
                data_list = read_xlsx(file_name)
                self.data = data_list
                self.mode = QStandardItemModel()
                for rows in data_list:
                    row = [QStandardItem(str(cell)) for cell in rows]
                    self.mode.appendRow(row)
                self.mode.itemChanged.connect(self.dealItemChanged)
                self.table_view.setModel(self.mode)
                # self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                self.table_view.resizeColumnsToContents()
                self.table_view.resizeRowsToContents()
                end = time.time()
                self.status_bar.showMessage('数据加载完毕,耗时{}秒'.format(end-start))
                self.setting.setEnabled(True)
            except Exception as e:
                print(e)
                pass

    def triggeredSave(self):
        self.status_bar.showMessage('保存文件', 5000)
        file_path, _ = QFileDialog.getSaveFileName(self, '保存文件', '../data',
                                                           'ALL Files(*);;xlsx(*.xlsx);;xls(*.xls);;csv(*.csv)')
        if file_path == '':
            return
        # 文件中写入数据
        try:
            wb = workbook.Workbook()
            wb.encoding = 'utf-8'
            wa = wb.active
            for item in self.data:
                # 过滤无效数据
                try:
                    if ''.join(item) == '':
                        continue
                except:
                    pass
                wa.append(item)
            wb.save(file_path)
            self.status_bar.showMessage('保存完毕！')
        except Exception as e:
            print(e)


    #数据变化信号处理
    def dealItemChanged(self,item):
        try:
            row,column = item.row(),item.column()
            self.data[row][column] = item.text()
        except Exception as e:
            print(e)
            pass

    #状态栏与工具栏的显示和隐藏
    def triggeredView(self,state):
        sender = self.sender().text()
        if sender == '工具栏':
            if state:
                self.tool_bar.show()
            else:
                self.tool_bar.hide()
        else:
            if state:
                self.status_bar.show()
            else:
                self.status_bar.hide()

    def triggeredNew(self):
        print('New')
        pass

    def triggeredFind(self):
        self.find_widget.show()

    #重载信号，实现ESC隐藏查找窗口
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.find_widget.hide()

    #聚焦到某个cell
    def positionFocus(self,x,y):
        self.table_view.verticalScrollBar().setSliderPosition(x)
        self.table_view.horizontalScrollBar().setSliderPosition(y)
        self.table_view.openPersistentEditor(self.mode.index(x, y))
        self.table_view.setFocus()

    #得到所以匹配项的位置
    def dataLocation(self):
        text = self.find_widget.line_edit1.text()
        self.res_pos = []
        flag = 0
        for i,row in enumerate(self.data):
            try:
                if ''.join(row) == '':
                    continue
            except:
                pass
            for j,cell in enumerate(row):
                if text == str(cell):
                    # print(i,j)
                    self.res_pos.append((i,j))
                    item = self.mode.item(i,j)
                    item.setBackground(QColor(255, 255, 0))
                    item.setForeground(QColor(255, 0, 0))
                    #转到到第一个匹配值的位置，并处于可编辑状态
                    if not flag:
                        flag = 1
                        self.positionFocus(i,j)
                        self.focus_pos = 0

    #向下跳转
    def downLocation(self):
        cnt = len(self.res_pos)
        if cnt == 0 or self.focus_pos == cnt-1:
            return
        try:
            self.table_view.closePersistentEditor(
                self.mode.index(self.res_pos[self.focus_pos][0],self.res_pos[self.focus_pos][1]))
            x, y = self.res_pos[self.focus_pos + 1]
            self.positionFocus(x,y)
            self.focus_pos += 1
        except Exception as e:
            print(e)

    # 向上跳转
    def upLocation(self):
        cnt = len(self.res_pos)
        if cnt == 0 or self.focus_pos == 0:
            return
        try:
            self.table_view.closePersistentEditor(
                self.mode.index(self.res_pos[self.focus_pos][0], self.res_pos[self.focus_pos][1]))
            x, y = self.res_pos[self.focus_pos - 1]
            self.positionFocus(x, y)
            self.focus_pos -= 1
        except Exception as e:
            print(e)


    def triggeredHideFind(self):
        if self.res_pos is not None and len(self.res_pos):
            self.table_view.closePersistentEditor(
                self.mode.index(self.res_pos[self.focus_pos][0], self.res_pos[self.focus_pos][1]))
            for item in self.res_pos:
                x,y = item
                item = self.mode.item(x,y)
                item.setBackground(QColor(255, 255, 255))
                item.setForeground(QColor(0, 0, 0))
        self.find_widget.hide()


    #不清楚如何修改cell值，替换功能暂时无法上线
    def onClickReplace(self):
        print('-'*50)
        cnt = len(self.res_pos)
        if self.res_pos is None or cnt == 0:
            return
        try:

            x, y = self.res_pos[self.focus_pos]
            text = self.find_widget.line_edit2.text()
            self.data[x][y] = text
            print(self.data[x][y])
        except Exception as e:
            print(e)

    def onClickReplaceAll(self):
        pass
    #设置变量
    def triggeredSetting(self):
        # 设置变量窗口
        var_list = self.data[0] if self.data[0][0]!='' else self.data[0][1:]
        self.dialog = VariableSettingWindow.VariableSettingWindowDemo(var_list)
        self.dialog.signal.sender.connect(self.getVarList)
        self.dialog.show()

    def getVarList(self,lst):
        self.var_list = lst
        # print(lst)






#xls,xlxs,csv
def read_xlsx(path):
    workbook = xlrd.open_workbook(path)
    sheet1 = workbook.sheet_by_index(0)
    rows = len(sheet1.col_values(0))
    data = [sheet1.row_values(i) for i in range(rows)]
    return data




class InputWindowDemo(QTabWidget):
    def __init__(self):
        super(InputWindowDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500,100,1000,900)
        self.setWindowIcon(QIcon('../image/导入.png'))

        #创建两个窗口
        #tab1：显示全部，tab2：只显示变量
        self.mode1 = QStandardItemModel(100,100)
        self.tab1 = WidgetDemo(self.mode1)
        self.mode2 = QStandardItemModel(100,100)
        self.tab2 = WidgetDemo(self.mode2)


        self.addTab(self.tab1,'数据视图')
        self.addTab(self.tab2,'变量视图')

        #tab放在底部
        self.setTabPosition(QTabWidget.TabPosition.South)
        #tab形状：设置为三角形：Triangular，圆角为：Rouned
        self.setTabShape(QTabWidget.Triangular)
        self.currentChanged.connect(self.getCurrentTab)

    def getCurrentTab(self,index):
        #得到数据视图中的数据
        all_data = self.tab1.data

        # print(all_data[0])
        # 当已经导入数据时设置变量视图
        if index == 1 and all_data is not None:
            cnt = 0
            for cell in all_data[0]:
                if cell != '':
                    self.mode2.setItem(cnt,0,QStandardItem(str(cell)))
                    cnt += 1



if __name__=='__main__':
    app = QApplication(sys.argv)
    window = InputWindowDemo()
    window.show()
    sys.exit(app.exec_())