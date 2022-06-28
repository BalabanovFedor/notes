# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_note.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_add_note(object):
    def setupUi(self, add_note):
        add_note.setObjectName("add_note")
        add_note.setFixedSize(330, 251)
        self.buttonBox = QtWidgets.QDialogButtonBox(add_note)
        self.buttonBox.setGeometry(QtCore.QRect(10, 210, 121, 31))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.note_text_PTE = QtWidgets.QPlainTextEdit(add_note)
        self.note_text_PTE.setGeometry(QtCore.QRect(0, 60, 321, 51))
        self.note_text_PTE.setObjectName("note_text_PTE")
        self.keys_PTE = QtWidgets.QPlainTextEdit(add_note)
        self.keys_PTE.setGeometry(QtCore.QRect(0, 160, 321, 41))
        self.keys_PTE.setObjectName("keys_PTE")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(add_note)
        self.dateTimeEdit.setGeometry(QtCore.QRect(0, 120, 321, 31))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.title_PTE = QtWidgets.QPlainTextEdit(add_note)
        self.title_PTE.setGeometry(QtCore.QRect(0, 0, 321, 51))
        self.title_PTE.setObjectName("title_PTE")

        self.retranslateUi(add_note)
        QtCore.QMetaObject.connectSlotsByName(add_note)

    def retranslateUi(self, add_note):
        _translate = QtCore.QCoreApplication.translate
        add_note.setWindowTitle(_translate("add_note", "Form"))
        self.note_text_PTE.setPlaceholderText(_translate("add_note", "Текст заметки"))
        self.keys_PTE.setPlaceholderText(_translate("add_note", "ключи поиска"))
        self.title_PTE.setPlaceholderText(_translate("add_note", "Заголовок"))
