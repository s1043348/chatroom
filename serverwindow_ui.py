# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\pc01\Documents\serverwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFont, QStandardItemModel, QStandardItem


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)   #Nickname
        self.label.setFont(QFont("Lucida console", 15))
        self.label.setGeometry(QtCore.QRect(5, 5, 100, 20))
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget) #User name
        self.lineEdit.setFont(QFont("Lucida console", 15))
        self.lineEdit.setGeometry(QtCore.QRect(110, 5, 110, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.label_2 = QtWidgets.QLabel(self.centralwidget) #password
        self.label_2.setFont(QFont("Lucida console", 15))
        self.label_2.setGeometry(QtCore.QRect(220, 5, 240, 20))
        self.label_2.setObjectName("label_2")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)   #User pswd
        self.lineEdit_2.setFont(QFont("Lucida console", 15))
        self.lineEdit_2.setGeometry(QtCore.QRect(320, 5, 155, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget) #Add button
        self.pushButton.setGeometry(QtCore.QRect(5, 30, 470, 30))
        self.pushButton.setObjectName("pushButton")

        self.label_question = QtWidgets.QLabel(self.centralwidget) #question label
        self.label_question.setFont(QFont("微軟正黑體", 20))
        self.label_question.setGeometry(QtCore.QRect(5, 65, 60, 30))
        self.label_question.setObjectName("label_question")

        self.lineEdit_question = QtWidgets.QLineEdit(self.centralwidget)  #edit question
        self.lineEdit_question.setFont(QFont("微軟正黑體", 20))
        self.lineEdit_question.setGeometry(QtCore.QRect(70, 65, 320, 30))
        self.lineEdit_question.setObjectName("lineEdit_2")

        self.pushButton_question = QtWidgets.QPushButton(self.centralwidget)  #question button
        self.pushButton_question.setGeometry(QtCore.QRect(395, 65, 80, 30))
        self.pushButton_question.setObjectName("pushButton_question")

        self.listView = QtWidgets.QListView(self.centralwidget) #score board on the left side
        self.listView.setGeometry(QtCore.QRect(5, 100, 470, 500))
        self.listView.setObjectName("listView")

        self.model = QStandardItemModel()       #user name checkbox in listview
        tsklist = [u'A', u'B', u'C', u'D', u'E']
        #tsklist[0], tsklist[1] = tsklist[1], tsklist[0] #simple swap case
        for task in tsklist:
            item = QStandardItem(task)
            item.setFont(QFont("微軟正黑體", 20))
            item.setCheckState(False)
            item.setCheckable(True)
            self.model.appendRow(item)
            self.listView.setModel(self.model)

        """
        self.check = QtWidgets.QCheckBox("hello", self.listView)
        self.check.setFont(QFont("微軟正黑體", 20))

        self.check2 = QtWidgets.QCheckBox("~~~~~~~~~~", self.check)
        self.check2.setFont(QFont("微軟正黑體", 20))
        """
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)   #kick button
        self.pushButton_2.setGeometry(QtCore.QRect(5, 605, 470, 30))
        self.pushButton_2.setObjectName("pushButton_2")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 355, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Server"))
        self.label.setText(_translate("MainWindow", "NickName"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Add"))
        self.pushButton_2.setText(_translate("MainWindow", "Kick"))
        self.label_question.setText(_translate("MainWindow", "題目"))
        self.pushButton_question.setText(_translate("MainWindow", "出題"))

