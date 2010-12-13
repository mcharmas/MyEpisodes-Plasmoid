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
from PyKDE4.plasma import Plasma
from PyKDE4 import plasmascript
from Config import *
from EpisodeSearchEngine import *
from EnginesConfig import *
from EpisodesList import *
import PyKDE4
import sip

class HelloWorldApplet(plasmascript.Applet):
    def __init(self,parent,atgs=None):
        plasmascript.Applet.__init__(self,parent)
        
    def init(self):        
        self.setAspectRatioMode(Plasma.IgnoreAspectRatio)
        self.setHasConfigurationInterface(True)
        
        self.settings = {}

        self.theme = Plasma.Svg(self)
        self.theme.setImagePath("widgets/background")
        self.setBackgroundHints(Plasma.Applet.StandardBackground)
        
        self.tabs = None
        self.button = None
        self.lastUpdateLabel = None
        self.timer = None
        
        self.lastUpdateText = 'Last update:'
        
        self.layout = QGraphicsLinearLayout(Qt.Vertical, self.applet)
        #self.layout.setSizePolicy(QSizePolicy(QSizePolicy.Expanding))
        
        self.searchEngines = []
          
        self.initList()            

        self.applet.setLayout(self.layout)

        self.resize(350, 300)
        
    def initList(self):
        self.configComplete = self.readConfig()
        
        print self.layout.count()
        for i in range(self.layout.count()):
            item = self.layout.itemAt(i)
            self.layout.removeAt(i)
            if item:            
                sip.delete(item)
        
        if self.button:
            sip.delete(self.button)
        
        if self.timer:
            sip.delete(self.timer)
            self.timer = None
            
          
        
        self.tabs = None
        self.button = None
        self.lastUpdateLabel = None
        
        if self.configComplete:
            self.tabs = Plasma.TabBar(self.applet)
            self.tabs.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
            self.button = Plasma.PushButton()
            self.button.setText("Refresh")
            self.button.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))
            
            self.lastUpdateLabel = Plasma.Label()            
            self.lastUpdateLabel.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))
            self.lastUpdateLabel.setMaximumHeight(13)
            #print self.lastUpdateLabel.sizeHint(0).height()
            self.lastUpdateLabel.setText('Last update: ?')            
            
            el1=EpisodesList(self.user, self.password, self.searchEngines, 'yesterday', self.applet)
            el2=EpisodesList(self.user, self.password, self.searchEngines, 'today', self.applet)
            el3=EpisodesList(self.user, self.password, self.searchEngines, 'tomorrow', self.applet) 

            if self.settings['enableTimer']:
                self.timer = QTimer(self)                
                self.timer.setInterval(self.settings['timerInterval'][0] * 60000)
                self.timer.timeout.connect(el1.updateData)  
                self.timer.timeout.connect(el2.updateData)
                self.timer.timeout.connect(el3.updateData)
                self.timer.timeout.connect(self.dateUpdate)
                self.timer.start()
                
            self.button.clicked.connect(el1.updateData)
            self.button.clicked.connect(el2.updateData)
            self.button.clicked.connect(el3.updateData)           
            self.button.clicked.connect(self.dateUpdate)      
            
            self.tabs.addTab('Yesterday', el1)
            self.tabs.addTab('Today', el2)
            self.tabs.addTab('Tomorrow', el3)
                    
            self.layout.addItem(self.tabs)
            if self.settings['showLastUpdate']:                  
                self.layout.addItem(self.lastUpdateLabel)
            
            if self.settings['showRefreshButton']:
                self.layout.addItem(self.button)

            self.dateUpdate()
                             
        else:
            self.list = Plasma.Label(self.applet)
            self.list.setText('<b><center>Applet is not configured.</center></b>')
            self.layout.addItem(self.list)
        
        if self.tabs:
            self.tabs.setCurrentIndex(1)
        
        self.update()
        
    def dateUpdate(self):
        if self.lastUpdateLabel <> None:
            date = QDateTime.currentDateTime()
            hour = date.toString('hh:mm:ss')
            date = date.toString('d MMM yyyy')
            self.lastUpdateLabel.setText(self.lastUpdateText+' '+hour+', '+date)

    def readConfig(self):            
        gc = self.config()
        self.user = gc.readEntry('login', '').toString()
        self.settings['login'] = self.user
        
        self.password = gc.readEntry('password', '').toString()
        self.settings['password'] = self.password
        
        #TODO: add this settings to configuration
        self.settings['showRefreshButton'] = gc.readEntry('showRefreshButton',False).toBool()
        self.settings['showLastUpdate'] = gc.readEntry('showLastUpdate', True).toBool()
        self.settings['enableTimer'] = gc.readEntry('enableTimer', True).toBool()
        self.settings['timerInterval'] = gc.readEntry('timerInterval', 5).toInt()
        
        #search engines config format title|url title1|url1
        engines = gc.readEntry('engines', '').toString()
        self.settings['engines']=engines
        self.searchEngines = []
        for en in engines.split(' '):
            if en:
                ep = en.split('|')
                self.searchEngines.append(EpisodeSearchEngine(ep[0], ep[1]))
        
        if self.user and self.password:
            return True
        else:
            return False          
    
    def createConfigurationInterface(self, parent):
        self.configWidget = Config(self, self.settings)
        self.engineConfigWidget = EnginesConfig(self.settings, self)
        parent.addPage(self.configWidget, 'Credentials')
        parent.addPage(self.engineConfigWidget, 'Search Engines')   
        parent.okClicked.connect(self.acceptConfig)
        parent.cancelClicked.connect(self.cancelConfig)                
        
    def showConfigurationInterface(self):
        dialog = KPageDialog()
        dialog.setFaceType(KPageDialog.List)
        dialog.setButtons( KDialog.ButtonCode(KDialog.Ok | KDialog.Cancel) )
        self.createConfigurationInterface(dialog)
        dialog.exec_()
        
    def acceptConfig(self):
        settings = self.configWidget.getSettings()
        gc = self.config()
        gc.writeEntry('login', settings['login'])
        gc.writeEntry('password', settings['password'])
        print settings['engines']
        gc.writeEntry('engines', settings['engines'])
        self.initList()
            
    def cancelConfig(self):
        pass
             
 
def CreateApplet(parent):
    return HelloWorldApplet(parent)
