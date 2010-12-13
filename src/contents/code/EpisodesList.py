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
from PyQt4 import *
from PyKDE4.plasma import Plasma
from PyKDE4 import plasmascript
from PyKDE4 import kdecore
from Episodes import *
from EpisodeWidget import *
import sip


class EpisodesList(Plasma.ScrollWidget):
    def __init__(self, user, password, searchEngines, type, parent=None):
        Plasma.ScrollWidget.__init__(self, parent)
        self.user = user
        self.password = password
        self.searchEngines = searchEngines        
        self.type = type
        self.widget = None

        self.initGetter()
        self.updateData()
        
        self.setHorizontalScrollBarPolicy(1)
    
    def initGetter(self):
        self.getter = EpisodeGetter(self.user, self.password, self.type, self)
        self.getter.completed.connect(self.refresh)        
    
    def refresh(self):                
        error = self.getter.getError()        
        episodes = self.getter.getData()
        
        if self.widget:
            sip.delete(self.widget)
            self.widget = None
        
        self.widget = QGraphicsWidget(self)
        
        self.wlayout = QGraphicsLinearLayout(Qt.Vertical, self.widget)
        self.wlayout.setSpacing(5)
        self.widget.setLayout(self.wlayout)
        
        size = 0

        if error == 0:
            if len(episodes):
                for e in episodes:
                    ep = EpisodeWidget(e, self.searchEngines, self.widget)
                    self.wlayout.addItem(ep)
                    size = size + ep.size().height()
                self.setWidget(self.widget)
            else: 
                self.showInfo('No episodes.')
        elif error == EpisodeGetter.ERROR_CONNECTION:
            self.showInfo('Error getting episodes.')
        elif error == EpisodeGetter.ERROR_CREDENTIALS:
            self.showInfo('Wrong credentials.')
        else:
            self.showInfo('Unknown error.')
        
        sip.delete(self.getter)
        self.initGetter()
        
        #self.update()
                
    def updateData(self):                
        #self.showInfo('Getting information from myepisodes.com.')
        if self.widget:
            sip.delete(self.widget)
        
        self.widget = Plasma.BusyWidget(self)
        self.setWidget(self.widget)
        self.getter.start()
        
    def showInfo(self, info):
        infoLabel = Plasma.Label(self)    
        infoLabel.setText('<center>'+info+'</center>')                
        self.setWidget(infoLabel)
        #self.update()        
    