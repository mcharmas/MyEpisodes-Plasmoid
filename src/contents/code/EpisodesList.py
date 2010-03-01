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
from Episodes import *
from EpisodeWidget import *

class EpisodesList(Plasma.ScrollWidget):
    def __init__(self, user, password, searchEngines, type, parent=None):
        Plasma.ScrollWidget.__init__(self, parent)
        self.info = 'Getting information from MyEpisodes'
        self.user = user
        self.password = password
        self.searchEngines = searchEngines        
        self.type = type
        #self.setSizePolicy(QSizePolicy(QSizePolicy.Minimum))
        self.setInfo()
        self.refresh()    
    
    def refresh(self):
        self.setInfo()
        error = 0
        try:
            self.episodes = self.getData()            
        except:
            error = 1

        self.widget = QGraphicsWidget(self)
        #self.widget.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        
        self.wlayout = QGraphicsLinearLayout(Qt.Vertical, self.widget)
        self.wlayout.setSpacing(5)
        self.widget.setLayout(self.wlayout)
        
        size = 0

        if not error:
            if len(self.episodes):
                for e in self.episodes:
                    ep = EpisodeWidget(e, self.searchEngines, self.widget)
                    self.wlayout.addItem(ep)
                    size = size + ep.size().height()
                self.setWidget(self.widget)
            else: 
                l = Plasma.Label(self)                
                l.setText('<center>No episodes today.</center>')
                self.setWidget(l)                
        else:
            l = Plasma.Label(self)
            l.setText('<center>Error getting episodes.</center>')
            self.setWidget(l)

        self.update()
        
    def setInfo(self):
        print "setting info"
        infoLabel = Plasma.Label(self)    
        infoLabel.setText(self.info)                
        self.setWidget(infoLabel)
        self.update()
        
        
    def getData(self):
        return getEpisodes(self.user, self.password, self.type)
