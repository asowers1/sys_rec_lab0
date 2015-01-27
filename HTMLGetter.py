__author__ = 'andrew'
import urllib.request


class HTMLGetter():
    def __init__(self):
        print ("init")

    def getHTMLFromURL(self, url):
        return urllib.request.urlopen(url).read()


