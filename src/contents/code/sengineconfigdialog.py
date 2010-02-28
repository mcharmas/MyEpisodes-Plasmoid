# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/sengineconfigdialog.ui'
#
# Created: Mon Mar  1 00:13:06 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SEngineConfigDialog(object):
    def setupUi(self, SEngineConfigDialog):
        SEngineConfigDialog.setObjectName("SEngineConfigDialog")
        SEngineConfigDialog.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(SEngineConfigDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.searchEnginesTable = QtGui.QTableView(SEngineConfigDialog)
        self.searchEnginesTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.searchEnginesTable.setProperty("showDropIndicator", False)
        self.searchEnginesTable.setDragDropOverwriteMode(True)
        self.searchEnginesTable.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.searchEnginesTable.setObjectName("searchEnginesTable")
        self.searchEnginesTable.horizontalHeader().setStretchLastSection(True)
        self.searchEnginesTable.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.searchEnginesTable)
        self.widget = QtGui.QWidget(SEngineConfigDialog)
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

        self.retranslateUi(SEngineConfigDialog)
        QtCore.QMetaObject.connectSlotsByName(SEngineConfigDialog)

    def retranslateUi(self, SEngineConfigDialog):
        SEngineConfigDialog.setWindowTitle(QtGui.QApplication.translate("SEngineConfigDialog", "Search Engine Config", None, QtGui.QApplication.UnicodeUTF8))
        self.newEngineButton.setText(QtGui.QApplication.translate("SEngineConfigDialog", "New Engine", None, QtGui.QApplication.UnicodeUTF8))
        self.saveButton.setText(QtGui.QApplication.translate("SEngineConfigDialog", "Save", None, QtGui.QApplication.UnicodeUTF8))

