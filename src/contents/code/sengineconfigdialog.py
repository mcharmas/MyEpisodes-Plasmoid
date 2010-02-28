# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/sengineconfigdialog.ui'
#
# Created: Sun Feb 28 17:49:07 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.searchEnginesTable = QtGui.QTableView(Form)
        self.searchEnginesTable.setObjectName("searchEnginesTable")
        self.verticalLayout.addWidget(self.searchEnginesTable)
        self.widget = QtGui.QWidget(Form)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.newEngineButton = QtGui.QPushButton(self.widget)
        self.newEngineButton.setObjectName("newEngineButton")
        self.horizontalLayout.addWidget(self.newEngineButton)
        spacerItem = QtGui.QSpacerItem(215, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.saveButton = QtGui.QPushButton(self.widget)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout.addWidget(self.saveButton)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.newEngineButton.setText(QtGui.QApplication.translate("Form", "New Engine", None, QtGui.QApplication.UnicodeUTF8))
        self.saveButton.setText(QtGui.QApplication.translate("Form", "Save", None, QtGui.QApplication.UnicodeUTF8))

