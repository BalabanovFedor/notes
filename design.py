# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(439, 376)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 40, 441, 251))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.plus_btn = QtWidgets.QPushButton(self.centralwidget)
        self.plus_btn.setGeometry(QtCore.QRect(380, 0, 41, 31))
        self.plus_btn.setObjectName("plus_btn")
        self.search_textedit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.search_textedit.setGeometry(QtCore.QRect(0, 0, 301, 31))
        self.search_textedit.setObjectName("search_textedit")
        self.search_btn = QtWidgets.QPushButton(self.centralwidget)
        self.search_btn.setGeometry(QtCore.QRect(300, 0, 61, 31))
        self.search_btn.setObjectName("search_btn")
        self.editmode_btn = QtWidgets.QPushButton(self.centralwidget)
        self.editmode_btn.setGeometry(QtCore.QRect(40, 300, 211, 31))
        self.editmode_btn.setObjectName("editmode_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 439, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.plus_btn.setText(_translate("MainWindow", "+"))
        self.search_textedit.setPlaceholderText(_translate("MainWindow", "поиск"))
        self.search_btn.setText(_translate("MainWindow", "поиск"))
        self.editmode_btn.setText(_translate("MainWindow", "режим редактирования"))
