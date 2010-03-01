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
from PyKDE4.plasma import Plasma
from PyKDE4 import plasmascript
from EpisodesList import *
from Config import *
from EpisodeSearchEngine import *
from EnginesConfig import *
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
        
        self.list = None
        self.refreshButton = None
        
        self.layout = QGraphicsLinearLayout(Qt.Vertical, self.applet)
        self.layout.setSizePolicy(QSizePolicy(QSizePolicy.Expanding))
        
        self.searchEngines = []
        self.searchEngines.append(EpisodeSearchEngine("Torrent-Damage", "http://www.torrent-damage.net/torrents.php?searchstr={show}+{series}x{episode}"))                
                                           
        self.initList()            

        self.applet.setLayout(self.layout)

        self.resize(300, 250)

    def initList(self):
        self.configComplete = self.readConfig()
        
        print self.layout.count()
        for i in range(self.layout.count()):
            item = self.layout.itemAt(i)
            self.layout.removeAt(i)
            if item:            
                sip.delete(item)
        
        if self.refreshButton:
            sip.delete(self.refreshButton)
        
        self.list = None
        self.refreshButton = None

        #self.icon = Plasma.Label(self.applet)
        #self.icon.setImage(unicode(self.package().path() + "contents/icons/myepisodes_logo.jpg"))        
        #self.layout.addItem(self.icon)

        if self.configComplete:
            self.list = EpisodesList(self.user, self.password, self.searchEngines, self.applet)
            self.refreshButton = Plasma.PushButton(self.applet)
            self.refreshButton.setText("Refresh")
            self.refreshButton.clicked.connect(self.list.refresh)
            self.layout.addItem(self.list)
            self.layout.addItem(self.refreshButton)                 
        else:
            self.list = Plasma.Label(self.applet)
            self.list.setText('<b>Applet is not configured.</b>')
            self.layout.addItem(self.list)
        self.update()

    def readConfig(self):            
        gc = self.config()
        self.user = gc.readEntry('login', '').toString()
        self.settings['login'] = self.user
        
        self.password = gc.readEntry('password', '').toString()
        self.settings['password'] = self.password
        
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
