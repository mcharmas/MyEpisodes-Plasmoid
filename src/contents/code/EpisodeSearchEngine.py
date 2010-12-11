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
from Episodes import *
import webbrowser

class EpisodeSearchEngine(QObject):
    def __init__(self, title, cstr):
        self.title = title
        self.cstr = cstr
        self.showString = "{show}"
        self.titleString = "{title}"
        self.seasonString = "{season}"
        self.episodeString = "{episode}"
        self.episode = None

    def search(self):
        nstr = str(self.cstr)
                
        nstr = nstr.replace(self.showString, str(self.episode.show))
        nstr = nstr.replace(self.titleString, self.episode.title)
        nstr = nstr.replace(self.seasonString, self.episode.season)
        nstr = nstr.replace(self.episodeString, self.episode.episodeNr)
        
        webbrowser.open_new(nstr)        
        
    def setEpisode(self, ep):
        self.episode = ep 