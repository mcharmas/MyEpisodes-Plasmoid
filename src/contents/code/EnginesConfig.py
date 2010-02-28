
"""Author: Michal Charmas
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

from sengineconfigdialog import Ui_SEngineConfigDialog

class EnginesConfig(QWidget, Ui_SEngineConfigDialog):
    def __init__(self, parent):
        QWidget.__init__(self)
        self.setupUi(self)
        self.parent = parent
                
        self.items = {'dupa':'jasio'}
        
        
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
        
        self.newEngineButton.clicked.connect(self.addRow)
        
    def addRow(self):        
        i1 = QStandardItem(QString(""))
        i2 = QStandardItem(QString(""))
        self.tableModel.appendRow([i1,i2])
        

