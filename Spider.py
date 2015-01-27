__author__ = 'andrew'

import HTMLGetter
import SoupMachine
import MLStripper
class Spider():
    html        = None
    soupMachine = None
    mlStriper   = None


    def __init__(self):
        htmlGetter = HTMLGetter.HTMLGetter()
        html = htmlGetter.getHTMLFromURL("http://archive.wired.com/wired/archive/12.10/tail_pr.html")
        #print(html)
        self.soupMachine = SoupMachine.SoupMachine(html)
        print(self.soupMachine.getTitle())