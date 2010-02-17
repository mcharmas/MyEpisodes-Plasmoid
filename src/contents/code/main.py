from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyKDE4.plasma import Plasma
from PyKDE4 import plasmascript
from EpisodesList import *
from Config import *
from hgext.mq import refresh
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
            self.list = EpisodesList(self.user, self.password, self.applet)
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
        
        if self.user and self.password:
            return True
        else:
            return False          
    
    def createConfigurationInterface(self, parent):
        self.configWidget = Config(self, self.settings)
        parent.addPage(self.configWidget, 'Credentials')   
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
        self.initList()
        
    
    def cancelConfig(self):
        pass
             
 
def CreateApplet(parent):
    return HelloWorldApplet(parent)