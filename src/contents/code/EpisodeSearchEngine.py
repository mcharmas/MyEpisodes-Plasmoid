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
        self.seriesString = "{series}"
        self.episodeString = "{episode}"
        self.episode = None

    def search(self):
        nstr = self.cstr
                
        nstr = nstr.replace(self.showString, str(self.episode.show))
        nstr = nstr.replace(self.titleString, self.episode.title)
        nstr = nstr.replace(self.seriesString, self.episode.series)
        nstr = nstr.replace(self.episodeString, self.episode.episodeNr)
        
        webbrowser.open_new(nstr)
        
    def setEpisode(self, ep):
        self.episode = ep 