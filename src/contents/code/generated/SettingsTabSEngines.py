# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/contents/ui/SettingsTabSEngines.ui'
#
# Created: Mon Dec 13 19:50:53 2010
#      by: PyQt4 UI code generator 4.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SettingsTabSEngines(object):
    def setupUi(self, SettingsTabSEngines):
        SettingsTabSEngines.setObjectName(_fromUtf8("SettingsTabSEngines"))
        SettingsTabSEngines.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(SettingsTabSEngines)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(SettingsTabSEngines)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.searchEnginesTable = QtGui.QTableView(SettingsTabSEngines)
        self.searchEnginesTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.searchEnginesTable.setProperty(_fromUtf8("showDropIndicator"), False)
        self.searchEnginesTable.setDragDropOverwriteMode(True)
        self.searchEnginesTable.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.searchEnginesTable.setObjectName(_fromUtf8("searchEnginesTable"))
        self.searchEnginesTable.horizontalHeader().setStretchLastSection(True)
        self.searchEnginesTable.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.searchEnginesTable)
        self.widget = QtGui.QWidget(SettingsTabSEngines)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.newEngineButton = QtGui.QPushButton(self.widget)
        self.newEngineButton.setObjectName(_fromUtf8("newEngineButton"))
        self.horizontalLayout.addWidget(self.newEngineButton)
        spacerItem = QtGui.QSpacerItem(215, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.saveButton = QtGui.QPushButton(self.widget)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.horizontalLayout.addWidget(self.saveButton)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(SettingsTabSEngines)
        QtCore.QMetaObject.connectSlotsByName(SettingsTabSEngines)

    def retranslateUi(self, SettingsTabSEngines):
        SettingsTabSEngines.setWindowTitle(QtGui.QApplication.translate("SettingsTabSEngines", "Search Engine Config", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SettingsTabSEngines", "In URL defninition you can use:\n"
"{show}, {title}, {season} and {episode} marks.", None, QtGui.QApplication.UnicodeUTF8))
        self.newEngineButton.setText(QtGui.QApplication.translate("SettingsTabSEngines", "New Engine", None, QtGui.QApplication.UnicodeUTF8))
        self.saveButton.setText(QtGui.QApplication.translate("SettingsTabSEngines", "Save", None, QtGui.QApplication.UnicodeUTF8))

