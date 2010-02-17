from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyKDE4.kio import *
from PyKDE4.kdeui import *
from PyKDE4.kdecore import *

from configdialog import Ui_ConfigDialog

class Config(QWidget, Ui_ConfigDialog):
    def __init__(self, parent, settings):
        QWidget.__init__(self)
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