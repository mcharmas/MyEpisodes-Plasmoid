"""
Author: Michal Charmas
"""

""" This file is part of MyEpisodes Plasmoid.

    MyEpisodes Plasmoid is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    MyEpisodes Plasmoid is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with MyEpisodes Plasmoid.  If not, see <http://www.gnu.org/licenses/>.
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyKDE4.kio import *
from PyKDE4.kdeui import *
from PyKDE4.kdecore import *

from generated.SettingsTabCredentials import Ui_SettingsTabCredentials
from generated.SettingsTabSEngines import Ui_SettingsTabSEngines
from generated.SettingsTabOptions import Ui_SettingsTabOptions
from generated.SettingsNewSEngineDialog import Ui_NewSearchEngineDialog


class ConfigCredentials(QWidget, Ui_SettingsTabCredentials):
    def __init__(self, settings, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.parent = parent
        self.settings = settings
        
        if 'login' in self.settings.keys():
            self.loginEdit.setText(settings['login'])
        if 'password' in self.settings.keys():
            self.passEdit.setText(settings['password'])
        
        self.loginEdit.textChanged.connect(self.loginChanged)
        self.passEdit.textChanged.connect(self.passwordChanged)
        
    def passwordChanged(self, string):
        self.settings['password'] = str(string)
    
    def loginChanged(self, string):
        self.settings['login'] = str(string)  
    
    def getSettings(self):
        return self.settings


class ConfigEngines(QWidget, Ui_SettingsTabSEngines):
    def __init__(self, settings, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.parent = parent
        self.settings = settings
        self.loadTable()        
        
        self.newEngineButton.clicked.connect(self.addRow)
        self.saveButton.clicked.connect(self.apply)
        
    def addRow(self):        
        i1 = QStandardItem(QString(""))
        i2 = QStandardItem(QString(""))
        self.tableModel.appendRow([i1,i2])
        
    def apply(self):
        error=0
        configString=""
        for i in range(self.tableModel.rowCount()):
            title = str(self.tableModel.item(i, 0).text())            
            url = str(self.tableModel.item(i, 1).text())
            if not title and not url:
                continue
            
            if not title and url:
                error=1
                self.showMsgBox('Title cannot be empty.')
                break
                
            if title and not url:
                error=1
                self.showMsgBox('URL cannot be empty.')
                break
            
            if title.find(' ')!=-1 or title.find('|')!=-1 or url.find(' ')!=-1 or url.find('|')!=-1:
                error=1
                self.showMsgBox('Title and URL cannot contain space or | characters.')
                break
            
            configString+=title+'|'+url+" "
                
        if not error:
            self.settings['engines']=configString
            self.loadTable()
            
    def showMsgBox(self, message):
        box = QMessageBox()
        box.setText(message)
        box.exec_()
            
    def loadTable(self):
        self.items = {}
        
        engines = self.settings['engines']
        for e in engines.split(' '):
            if e:
                en = e.split('|')
                self.items[en[0]]=en[1]
        
        self.tableModel = QStandardItemModel(len(self.items), 2)
        self.tableModel.setHorizontalHeaderLabels(["Name", "Search URL"])
        ind=0
        for i in self.items.keys():
            sitem1 = QStandardItem(QString(i))
            sitem2 = QStandardItem(QString(self.items[i]))
            self.tableModel.setItem(ind, 0, sitem1)
            self.tableModel.setItem(ind, 1, sitem2)
            ind+=1
            
        self.searchEnginesTable.setModel(self.tableModel)

class ConfigOptions(QWidget, Ui_SettingsTabOptions):
    def __init__(self, settings, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.parent = parent
        self.settings = settings
        
        self.refreshButtonBox.stateChanged.connect(self.refreshBoxChanged)
        self.updateInfoBox.stateChanged.connect(self.showLabelBoxChanged)
        self.automaticUpdatesBox.stateChanged.connect(self.automaticUpdatesBoxChanged)
        self.updateIntervalBox.valueChanged.connect(self.updateIntervalBoxChanged)
        
        if self.settings['showRefreshButton']:
            self.refreshButtonBox.setCheckState(2)
        
        if self.settings['showLastUpdate']:
            self.updateInfoBox.setCheckState(2)
            
        if self.settings['enableTimer']:
            self.automaticUpdatesBox.setCheckState(2)
            
        self.updateIntervalBox.setValue(self.settings['timerInterval'])
    
    def refreshBoxChanged(self, x):
        if x == 0:
            res = False
            if not self.settings['enableTimer']:
                self.automaticUpdatesBox.setCheckState(2)
                self.automaticUpdatesBoxChanged(2) 
        else:
            res = True
        self.settings['showRefreshButton'] = res
    
    def showLabelBoxChanged(self, x):
        if x == 0:
            res = False
        else:
            res = True
        self.settings['showLastUpdate'] = res
    
    def automaticUpdatesBoxChanged(self, x):
        if x == 0:
            self.updateIntervalBox.setEnabled(False)
            self.settings['enableTimer'] = False
            self.refreshBoxChanged(2)
            self.refreshButtonBox.setCheckState(2)
        else:
            self.updateIntervalBox.setEnabled(True)
            self.settings['enableTimer'] = True
    
    def updateIntervalBoxChanged(self, x):
        self.settings['timerInterval'] = x
    
    def getSettings(self):
        return self.settings