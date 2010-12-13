# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/contents/ui/SettingsNewSEngineDialog.ui'
#
# Created: Mon Dec 13 19:30:15 2010
#      by: PyQt4 UI code generator 4.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_NewSearchEngineDialog(object):
    def setupUi(self, NewSearchEngineDialog):
        NewSearchEngineDialog.setObjectName(_fromUtf8("NewSearchEngineDialog"))
        NewSearchEngineDialog.resize(460, 146)
        self.verticalLayout = QtGui.QVBoxLayout(NewSearchEngineDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(NewSearchEngineDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.frame = QtGui.QFrame(NewSearchEngineDialog)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.nameEdit = QtGui.QLineEdit(self.frame)
        self.nameEdit.setObjectName(_fromUtf8("nameEdit"))
        self.gridLayout.addWidget(self.nameEdit, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.urlEdit = QtGui.QLineEdit(self.frame)
        self.urlEdit.setObjectName(_fromUtf8("urlEdit"))
        self.gridLayout.addWidget(self.urlEdit, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.widget = QtGui.QWidget(NewSearchEngineDialog)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.addButton = QtGui.QPushButton(self.widget)
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.horizontalLayout.addWidget(self.addButton)
        spacerItem1 = QtGui.QSpacerItem(310, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.cancelButton = QtGui.QPushButton(self.widget)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout.addWidget(self.cancelButton)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(NewSearchEngineDialog)
        QtCore.QMetaObject.connectSlotsByName(NewSearchEngineDialog)

    def retranslateUi(self, NewSearchEngineDialog):
        NewSearchEngineDialog.setWindowTitle(QtGui.QApplication.translate("NewSearchEngineDialog", "New Search Engine", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("NewSearchEngineDialog", "In URL defninition you can use {show}, {title}, {series} and {episode} marks.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("NewSearchEngineDialog", "Engine Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("NewSearchEngineDialog", "URL:", None, QtGui.QApplication.UnicodeUTF8))
        self.addButton.setText(QtGui.QApplication.translate("NewSearchEngineDialog", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("NewSearchEngineDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

