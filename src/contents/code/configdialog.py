# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/configdialog.ui'
#
# Created: Sun Feb  7 13:20:24 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ConfigDialog(object):
    def setupUi(self, ConfigDialog):
        ConfigDialog.setObjectName("ConfigDialog")
        ConfigDialog.resize(289, 169)
        self.gridLayout = QtGui.QGridLayout(ConfigDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtGui.QGroupBox(ConfigDialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.loginEdit = QtGui.QLineEdit(self.groupBox)
        self.loginEdit.setObjectName("loginEdit")
        self.gridLayout_2.addWidget(self.loginEdit, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.passEdit = QtGui.QLineEdit(self.groupBox)
        self.passEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passEdit.setObjectName("passEdit")
        self.gridLayout_2.addWidget(self.passEdit, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 1, 1, 1)

        self.retranslateUi(ConfigDialog)
        QtCore.QMetaObject.connectSlotsByName(ConfigDialog)

    def retranslateUi(self, ConfigDialog):
        ConfigDialog.setWindowTitle(QtGui.QApplication.translate("ConfigDialog", "MyEpisodes Config", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ConfigDialog", "MyEpisodes Credentials", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ConfigDialog", "Login:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ConfigDialog", "Password:", None, QtGui.QApplication.UnicodeUTF8))

