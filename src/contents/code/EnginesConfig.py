
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
    