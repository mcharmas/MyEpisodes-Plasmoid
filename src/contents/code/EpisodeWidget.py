from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Episodes import *
from PyKDE4.plasma import Plasma
from PyKDE4 import plasmascript

class EpisodeWidget(Plasma.Frame):
    
    def __init__(self, episode, parent):
        Plasma.Frame.__init__(self, parent)
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
        
        self.setMinimumWidth(250)
        self.setMinimumHeight(self.titleLabel.size().height() + self.seriesWidget.size().height())
        
        
