from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyKDE4.plasma import Plasma
from PyKDE4 import plasmascript
from Episodes import *
from EpisodeWidget import *

class EpisodesList(Plasma.ScrollWidget):
    def __init__(self, user, password, parent=None):
        Plasma.ScrollWidget.__init__(self, parent)
        self.info = 'Getting information from MyEpisodes'
        self.user = user
        self.password = password        
        self.setInfo()
        self.refresh()    
    
    def refresh(self):
        self.setInfo()
        try:
            self.episodes = self.getData()
        except:
            self.episodes = None

        self.widget = QGraphicsWidget(self)
        self.widget.setSizePolicy(QSizePolicy(QSizePolicy.Expanding))
        self.wlayout = QGraphicsLinearLayout(Qt.Vertical, self.widget)
        self.wlayout.setSpacing(5)
        self.widget.setLayout(self.wlayout)
        
        size = 0

        if self.episodes:
            if len(self.episodes):
                for e in self.episodes:
                    ep = EpisodeWidget(e, self.widget)
                    self.wlayout.addItem(ep)
                    size = size + ep.size().height()
                self.setWidget(self.widget)
            else: 
                l = Plasma.Label(self)
                l.setText('No episodes today.')
                self.setWidget(l)                
        else:
            l = Plasma.Label(self)
            l.setText('Error getting episodes.')
            self.setWidget(l)

        self.update()
        
    def setInfo(self):
        print "setting info"
        infoLabel = Plasma.Label(self)    
        infoLabel.setText(self.info)                
        self.setWidget(infoLabel)
        self.update()
        
        
    def getData(self):
        return getEpisodes(self.user, self.password)
