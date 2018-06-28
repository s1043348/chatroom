# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\pc01\Documents\clientwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QMessageBox, QLineEdit)
from PyQt5.QtGui import QFont


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 760)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)   # 目前聊天室 x 人
        self.label.setGeometry(QtCore.QRect(35, 10, 150, 16))
        self.label.setFont(QFont("微軟正黑體", 12))
        self.label.setAutoFillBackground(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)  # Nickname
        self.label_2.setFont(QFont("Lucida console", 15))
        self.label_2.setGeometry(QtCore.QRect(15, 30, 100, 30))
        self.label_2.setObjectName("label_2")

        self.label_turn = QtWidgets.QLabel(self.centralwidget)  # host turn
        self.label_turn.setFont(QFont("微軟正黑體", 15))
        self.label_turn.setGeometry(QtCore.QRect(600, 0, 400, 30))
        self.label_turn.setObjectName("label_turn")

        self.label_remain_t = QtWidgets.QLabel(self.centralwidget)  # remaining time
        self.label_remain_t.setFont(QFont("微軟正黑體", 12))
        self.label_remain_t.setGeometry(QtCore.QRect(900, 0, 200, 30))
        self.label_remain_t.setObjectName("label_remain_t")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)  # user name
        self.lineEdit.setFont(QFont("Lucida console", 12))
        self.lineEdit.setGeometry(QtCore.QRect(120, 30, 110, 30))
        self.lineEdit.setObjectName("lineEdit")

        self.label_pswd = QtWidgets.QLabel(self.centralwidget)  # user pswd
        self.label_pswd.setFont(QFont("Lucida console", 15))
        self.label_pswd.setGeometry(QtCore.QRect(15, 65, 100, 30))
        self.label_pswd.setObjectName("label_pswd")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)  # input pswd
        self.lineEdit_2.setFont(QFont("Lucida console", 12))
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 65, 110, 30))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)  # input change pswd
        self.label_3.setFont(QFont("Lucida console", 10))
        self.label_3.setGeometry(QtCore.QRect(15, 100, 100, 30))
        self.label_3.setObjectName("label_3")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)  # login
        self.pushButton.setGeometry(QtCore.QRect(15, 140, 105, 30))
        self.pushButton.setObjectName("pushButton")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)  # user change pswd
        self.lineEdit_3.setFont(QFont("Lucida console", 12))
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 100, 110, 30))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setEchoMode(QLineEdit.Password)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)   # update pswd
        self.pushButton_2.setGeometry(QtCore.QRect(125, 140, 105, 30))
        self.pushButton_2.setObjectName("pushButton_2")

        self.tableView = QtWidgets.QTableView(self.centralwidget)  # score board on the left side
        self.tableView.setGeometry(QtCore.QRect(5, 200, 235, 500))
        self.tableView.setObjectName("tableView")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)  # Chat room
        self.textBrowser.setGeometry(QtCore.QRect(1190, 5, 235, 320))
        self.textBrowser.setObjectName("textBrowser")

        self.textBrowser_ans = QtWidgets.QTextBrowser(self.centralwidget)  # Answer room
        self.textBrowser_ans.setGeometry(QtCore.QRect(1190, 365, 235, 320))
        self.textBrowser_ans.setObjectName("textBrowser_ans")

        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)   # input send message
        self.lineEdit_4.setFont(QFont("微軟正黑體", 12))
        self.lineEdit_4.setGeometry(QtCore.QRect(1190, 330, 200, 30))
        self.lineEdit_4.setInputMask("")
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)   # send button
        self.pushButton_3.setGeometry(QtCore.QRect(1395, 330, 40, 30))
        self.pushButton_3.setObjectName("pushButton_3")

        self.lineEdit_ans = QtWidgets.QLineEdit(self.centralwidget)  # input ans message
        self.lineEdit_ans.setFont(QFont("微軟正黑體", 12))
        self.lineEdit_ans.setGeometry(QtCore.QRect(1190, 690, 200, 30))
        self.lineEdit_ans.setInputMask("")
        self.lineEdit_ans.setObjectName("lineEdit_ans")

        self.pushButton_ans = QtWidgets.QPushButton(self.centralwidget)  # ans button
        self.pushButton_ans.setGeometry(QtCore.QRect(1395, 690, 40, 30))
        self.pushButton_ans.setObjectName("pushButton_ans")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 389, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Client"))
        self.label.setText(_translate("MainWindow", "目前聊天室有0人"))
        self.label_2.setText(_translate("MainWindow", "NickName"))
        self.label_pswd.setText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.label_3.setText(_translate("MainWindow", "Change pswd"))
        self.pushButton_2.setText(_translate("MainWindow", "update password"))
        self.pushButton_3.setText(_translate("MainWindow", "Send"))
        self.pushButton_ans.setText(_translate("Mainwindow", "Ans"))
        self.label_turn.setText(_translate("MainWindow", "目前輪到 某某某 出題"))
        self.label_remain_t.setText(_translate("MainWindow", "剩餘時間: 30 秒"))
