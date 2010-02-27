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
        self.series = self.episode.split('x')[0]
        self.episodeNr = self.episode.split('x')[1]
        
    def str(self):
        return self.show + " " + self.episode + " " + self.title + " " + self.date 


def getEpisodes(username, password):    
    password = md5(str(password))
    host = 'myepisodes.com'
    port = 80
    episodes = []

    connection = HTTPConnection(host, port)
    connection.request('GET', '/rss.php?feed=all&uid='+str(username)+'&pwdmd5='+password.hexdigest())
    resp = connection.getresponse()
    print resp.status, resp.reason, resp.getheader('Location')
    if resp.status != 200:
        connection.close()
        raise Exception('Bad URL?!')
    
    data = resp.read()
    connection.close()
    if not data:
        raise Exception('Bad credentials.')


    DOMTree = minidom.parseString(data)
    cNodes = DOMTree.childNodes
    try:    
        for i in cNodes[0].getElementsByTagName("item"):
            title = i.getElementsByTagName("title")[0].childNodes[0].toxml()
            title = title[1:-1]
            title = title.split('][')
            link = i.getElementsByTagName("link")[0].childNodes[0].toxml()
            episodes.append(Episode(title[0], title[1], title[2], title[3], link))
    except:
        return []

    for e in episodes:
        print e.str()
        
    return episodes
    