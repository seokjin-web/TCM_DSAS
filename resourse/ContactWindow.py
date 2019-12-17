#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/12/14 0014 20:10
#@Author  :    tb_youth
#@FileName:    ContactWindow.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
反馈建议：
实现发送邮件功能：
from 15270684004@163.com
to 2638961251@qq.com
'''

import sys
from PyQt5.QtWidgets import QWidget,QApplication,QMessageBox
from PyQt5.QtWidgets import QTextEdit,QPushButton,QLineEdit,QLabel
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtWidgets import QFormLayout,QHBoxLayout,QVBoxLayout

import smtplib
from email.mime.text import MIMEText
from resourse import Morse

class SendEmail():
    def __init__(self,theme,content):
        '''
        皮一下~~
        '''
        from_address = '01111 00000 00111 11000 11111 10000 11100 00001 11111 11111 00001 011010 01111 10000 00011 010101 1010 111 11'
        key = '- -... -.-- --- ..- - .... -.... -.... -....'
        to_address = '..--- -.... ...-- ---.. ----. -.... .---- ..--- ..... .---- .--.-. --.- --.- .-.-.- -.-. --- --'
        morse = Morse.MorseDemo()

        self.__smtp_server = 'smtp.163.com'
        self.__sender = morse.decode(from_address.replace('0', '.').replace('1', '-'))[1]
        self.__key = morse.decode(key)[0].lower()
        self.__receivers = [morse.decode(to_address.replace('0', '.').replace('1', '-'))[1],self.__sender]
        self.__theme = theme
        self.__content = content
        self.__new_msg = MIMEText(self.__content,'plain','utf-8')

        self.__new_msg['Subject'] = self.__theme
        self.__new_msg['From'] = self.__sender
        self.__new_msg['To'] = ','.join(self.__receivers)


    def send(self):
        try:
            server = smtplib.SMTP(self.__smtp_server, port=25)
            server.set_debuglevel(1)
            server.login(self.__sender, self.__key)
            server.sendmail(self.__new_msg['From'], self.__new_msg['To'].split(','), self.__new_msg.as_string())
            server.quit()
            print('发送成功！')
            return True
        except Exception as e:
            print('出错啦~')
            print(e)
            return False

class ConcatWindow(QWidget):
    def __init__(self):
        super(ConcatWindow,self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(800,800)
        self.setWindowTitle('反馈建议')
        icon = QIcon()
        icon.addPixmap(QPixmap('../image/反馈.png'), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)


        self.label1 = QLabel('邮件主题：')
        self.line_edit1 = QLineEdit()
        self.line_edit1.setPlaceholderText('反馈 or 建议')
        self.line_edit2 = QLineEdit()
        self.label2 = QLabel('联系方式：')
        self.line_edit2.setPlaceholderText('QQ:xxx or Tel:xxx')

        self.label3 = QLabel('邮件内容：')
        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText('邮件内容')
        # self.button_cancel = QPushButton('取消')
        self.button_send = QPushButton('发送')
        self.button_clear = QPushButton('清空')

        hlayout = QHBoxLayout()
        hlayout.addStretch()
        hlayout.addWidget(self.button_clear)
        # hlayout.addWidget(self.button_cancel)
        hlayout.addWidget(self.button_send)
        hlayout.setStretch(0,1)
        hlayout.setStretch(1,1)
        hlayout.setStretch(2,1)
        hlayout.setStretch(3,1)
        hlayout.setSpacing(10)

        formlayout = QFormLayout()
        formlayout.addRow(self.label1, self.line_edit1)
        formlayout.addRow(self.label2, self.line_edit2)
        formlayout.setSpacing(10)

        vlayout1 = QVBoxLayout()
        vlayout1.addWidget(self.text_edit)
        vlayout1.addItem(hlayout)
        vlayout1.setStretch(0,8)
        vlayout1.setStretch(1,1)
        vlayout1.setSpacing(10)


        vlayout2 = QVBoxLayout()
        vlayout2.addItem(formlayout)
        vlayout2.addItem(vlayout1)

        self.setLayout(vlayout2)

        self.button_send.clicked.connect(self.onClickSend)
        self.button_clear.clicked.connect(self.text_edit.clear)
        # self.button_cancel.clicked.connect(self.close)

    def onClickSend(self):
        theme = self.line_edit1.text()
        contact_information = self.line_edit2.text()
        text = self.text_edit.toPlainText()
        if theme == '' or contact_information == '' or text == '':
            return
        content = 'Content:\n{}\nContact Information:{}'.format(text,contact_information)
        print(content)
        try:
            sender = SendEmail(theme,content)
            result = sender.send()
            if result:
                QMessageBox.information(self, '成功', '您的反馈建议已送达!', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            else:
                QMessageBox.information(self, '失败', '请检查主题内容是否合理!', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        except:
           pass









if __name__=='__main__':
    app = QApplication(sys.argv)
    window = ConcatWindow()
    window.show()
    sys.exit(app.exec_())