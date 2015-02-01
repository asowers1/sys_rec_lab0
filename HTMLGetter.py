__author__ = 'andrew'
import urllib.request


class HTMLGetter():

    def getHTMLFromURL(self, url):

        response = urllib.request.urlopen(url)
        the_page = response.read()
        text = the_page.decode("iso-8859-1")
        return text

