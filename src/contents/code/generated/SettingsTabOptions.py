# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/contents/ui/SettingsTabOptions.ui'
#
# Created: Mon Dec 13 19:30:17 2010
#      by: PyQt4 UI code generator 4.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SettingsTabOptions(object):
    def setupUi(self, SettingsTabOptions):
        SettingsTabOptions.setObjectName(_fromUtf8("SettingsTabOptions"))
        SettingsTabOptions.resize(389, 292)
        self.verticalLayout = QtGui.QVBoxLayout(SettingsTabOptions)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(SettingsTabOptions)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.refreshButtonBox = QtGui.QCheckBox(self.groupBox)
        self.refreshButtonBox.setObjectName(_fromUtf8("refreshButtonBox"))
        self.verticalLayout_2.addWidget(self.refreshButtonBox)
        self.updateInfoBox = QtGui.QCheckBox(self.groupBox)
        self.updateInfoBox.setObjectName(_fromUtf8("updateInfoBox"))
        self.verticalLayout_2.addWidget(self.updateInfoBox)
        self.automaticUpdatesBox = QtGui.QCheckBox(self.groupBox)
        self.automaticUpdatesBox.setObjectName(_fromUtf8("automaticUpdatesBox"))
        self.verticalLayout_2.addWidget(self.automaticUpdatesBox)
        self.widget = QtGui.QWidget(self.groupBox)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.updateIntervalBox = QtGui.QSpinBox(self.widget)
        self.updateIntervalBox.setMinimum(1)
        self.updateIntervalBox.setMaximum(30)
        self.updateIntervalBox.setObjectName(_fromUtf8("updateIntervalBox"))
        self.horizontalLayout.addWidget(self.updateIntervalBox)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.widget)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(SettingsTabOptions)
        QtCore.QMetaObject.connectSlotsByName(SettingsTabOptions)

    def retranslateUi(self, SettingsTabOptions):
        SettingsTabOptions.setWindowTitle(QtGui.QApplication.translate("SettingsTabOptions", "SettingsTabOptions", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("SettingsTabOptions", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.refreshButtonBox.setText(QtGui.QApplication.translate("SettingsTabOptions", "Show Refresh button", None, QtGui.QApplication.UnicodeUTF8))
        self.updateInfoBox.setText(QtGui.QApplication.translate("SettingsTabOptions", "Show last update info", None, QtGui.QApplication.UnicodeUTF8))
        self.automaticUpdatesBox.setText(QtGui.QApplication.translate("SettingsTabOptions", "Enable automatic updates", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SettingsTabOptions", "Update inteval (hour):", None, QtGui.QApplication.UnicodeUTF8))

