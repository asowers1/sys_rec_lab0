__author__ = 'andrew'

from bs4 import BeautifulSoup

class SoupMachine():

    soup = None
    def __init__(self, html_doc):
        self.soup = BeautifulSoup(html_doc)
    def getTitle(self):
        return self.soup.title
    def getTitleName(self):
        return self.soup.title.name
    def getAllText(self):
        return self.soup.get_text()