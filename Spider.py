__author__ = 'andrew'

import HTMLGetter
import SoupMachine
import MLStripper
import nltk
import nltk.data
import re
class Spider():
    html        = None
    soupMachine = None
    mlStriper   = None


    def __init__(self):
        htmlGetter = HTMLGetter.HTMLGetter()
        html = htmlGetter.getHTMLFromURL("http://archive.wired.com/wired/archive/12.10/tail_pr.html")
        self.soupMachine = SoupMachine.SoupMachine(html)
        strippedhtml = self.removeComments(self.removeHtmlComments(self.soupMachine.getAllText()))
        print(nltk.word_tokenize(strippedhtml))

    def removeComments(self,string):
        string = re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,string) # remove all occurance streamed comments (/*COMMENT */) from string
        string = re.sub(re.compile("//.*?\n" ) ,"" ,string) # remove all occurance singleline comments (//COMMENT\n ) from string
        return string

    def removeHtmlComments(self,string):
        string = re.sub(re.compile("<!--.*?-->",re.DOTALL ) ,"" ,string) # remove all occurance streamed comments (/*COMMENT */) from string
        return string