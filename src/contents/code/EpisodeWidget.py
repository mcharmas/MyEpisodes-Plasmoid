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
from Episodes import *
from PyKDE4.plasma import Plasma
from PyKDE4 import plasmascript

class EpisodeWidget(Plasma.Frame):
    
    def __init__(self, episode, searchEngines, parent):
        Plasma.Frame.__init__(self, parent)
        self.episode = episode
        self.setFrameShadow(3)       
        self.setLayout(QGraphicsLinearLayout(Qt.Vertical, self))                
        
        #setting up series widget
        self.seriesWidget = QGraphicsWidget(self)
        self.seriesWidget.setLayout(QGraphicsLinearLayout(Qt.Horizontal, self.seriesWidget))
        
        self.showLabel = Plasma.Label(self.seriesWidget)
        self.showLabel.setAlignment(Qt.AlignLeft)
        self.showLabel.setText("<b>"+episode.show + "</b>")

        self.epLabel = Plasma.Label(self.seriesWidget)
        self.epLabel.setAlignment(Qt.AlignRight)
        self.epLabel.setText("<b>"+episode.episode+"</b>")
        
        self.seriesWidget.layout().addItem(self.showLabel)
        self.seriesWidget.layout().addItem(self.epLabel)
        #s#########################
                        
        self.titleLabel = Plasma.Label(self)
        self.titleLabel.setAlignment(Qt.AlignCenter)
        self.titleLabel.setText(episode.title+' ('+episode.date+')\n')
        
        self.layout().addItem(self.seriesWidget)
        self.layout().addItem(self.titleLabel)
        
        self.searchEngines = searchEngines                            
        
        self.setMinimumWidth(250)
        self.setMinimumHeight(self.titleLabel.size().height() + self.seriesWidget.size().height())
                
    def contextMenuEvent(self,ev):        
        if not len(self.searchEngines):
            return
        
        menu = QMenu()
        for eng in self.searchEngines:
            eng.setEpisode(self.episode)
            act = QAction(QString(eng.title), menu)
            act.triggered.connect(eng.search)
            menu.addAction(act)
            
        menu.exec_(ev.screenPos())        
