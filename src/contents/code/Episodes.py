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
from PyKDE4.kdecore import KUrl
from PyKDE4.kio import *
from hashlib import md5
from httplib import HTTPConnection
from xml.dom import minidom
import sys
import time

class Episode:
    def __init__(self, show, episode, title, date, link):
        self.show = show[1:-1]
        self.episode = episode[1:-1]
        self.title = title[1:-1]
        self.date = date[1:-1]
        self.link = link
        self.season = self.episode.split('x')[0]
        self.episodeNr = self.episode.split('x')[1]
        
    def str(self):
        return self.show + " " + self.episode + " " + self.title + " " + self.date 


class EpisodeGetter(QObject):
    
    ERROR_NO = 0
    ERROR_CONNECTION = 1
    ERROR_CREDENTIALS = 2
    ERROR_PARSING = 3
    
    completed = pyqtSignal()
    
    def __init__(self, username, password, type, parent=None):
        QObject.__init__(self,parent)
        self.username = username
        self.password = md5(str(password))
        self.type = type
        self.host = 'http://myepisodes.com/'
        self.port = 80
        self.url = self.host+'/rss.php?feed='+str(self.type)+'&uid='+str(self.username)+'&pwdmd5='+self.password.hexdigest()
        self.data = None
        self.error = self.ERROR_NO
        self.job = None
            
    def getError(self):
         return self.error
     
    def getData(self):
         return self.data
     
    def start(self):
        url = KUrl(self.url)
        self.job = KIO.storedGet(url, KIO.Reload, KIO.HideProgressInfo)
        self.connect(self.job, SIGNAL("result(KJob*)"), self.resultData)    
        
    def resultData(self, job):
        print self.type + ': Got data.'
        if job.error() <> 0:
            self.error = self.ERROR_CONNECTION
            print 'Error getting feed: '+str(job.error())+' '+job.errorText()
        else:
            self.data = self.parseFeed(job.data())            
        
        self.completed.emit()
    
    def parseFeed(self, dataToParse):
        if not dataToParse:
            self.error = self.ERROR_CREDENTIALS
            return None
            
        episodes = []
        DOMTree = minidom.parseString(dataToParse)
        cNodes = DOMTree.childNodes
        try:    
            for i in cNodes[0].getElementsByTagName("item"):
                title = i.getElementsByTagName("title")[0].childNodes[0].toxml()
                if(title == 'No Episodes'):
                    return []
                title = title[1:-1]
                title = title.split('][')
                link = i.getElementsByTagName("link")[0].childNodes[0].toxml()
                episodes.append(Episode(title[0], title[1], title[2], title[3], link))
        except:
            self.error = self.ERROR_PARSING
            return None
    
        print "##### EPISODES ######"
        for e in episodes:
            print e.str()
        print "### END EPISODES ####"
            
        return episodes
    