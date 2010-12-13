# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/contents/ui/settings_tab_credentials.ui'
#
# Created: Mon Dec 13 02:53:48 2010
#      by: PyQt4 UI code generator 4.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SettingsTabCredentials(object):
    def setupUi(self, SettingsTabCredentials):
        SettingsTabCredentials.setObjectName(_fromUtf8("SettingsTabCredentials"))
        SettingsTabCredentials.resize(289, 169)
        self.gridLayout = QtGui.QGridLayout(SettingsTabCredentials)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(SettingsTabCredentials)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.loginEdit = QtGui.QLineEdit(self.groupBox)
        self.loginEdit.setObjectName(_fromUtf8("loginEdit"))
        self.gridLayout_2.addWidget(self.loginEdit, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.passEdit = QtGui.QLineEdit(self.groupBox)
        self.passEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passEdit.setObjectName(_fromUtf8("passEdit"))
        self.gridLayout_2.addWidget(self.passEdit, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 1, 1, 1)

        self.retranslateUi(SettingsTabCredentials)
        QtCore.QMetaObject.connectSlotsByName(SettingsTabCredentials)

    def retranslateUi(self, SettingsTabCredentials):
        SettingsTabCredentials.setWindowTitle(QtGui.QApplication.translate("SettingsTabCredentials", "MyEpisodes Config", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("SettingsTabCredentials", "MyEpisodes Credentials", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SettingsTabCredentials", "Login:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("SettingsTabCredentials", "Password:", None, QtGui.QApplication.UnicodeUTF8))

