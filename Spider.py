__author__ = 'andrew'

import HTMLGetter
import SoupMachine
from collections import defaultdict
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
        title = self.soupMachine.getTitle()
        print(title)

        strippedhtml = self.removePunc(self.removeComments(self.removeHtmlComments(self.soupMachine.getAllText())))
        tokens = nltk.word_tokenize(strippedhtml)
        print("tokens: " + str(len(tokens)))
        tokens = self.removeUpperFromTokenList(tokens)
        dict = self.convertListToDictionary(tokens)
        print(dict)

    def removeComments(self, string):
        string = re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,string) # remove all occurance streamed comments (/*COMMENT */) from string
        string = re.sub(re.compile("//.*?\n" ) ,"" ,string) # remove all occurance singleline comments (//COMMENT\n ) from string
        return string

    def removeHtmlComments(self, string):
        string = re.sub(re.compile("<!--.*?-->",re.DOTALL ) ,"" ,string) # remove all occurance HTML comments (<!-- -->) from string
        return string

    def removePunc(self, string):
        string = re.sub(re.compile("[^-'\w\s]",re.DOTALL ) ,"" ,string) # remove all occurances punctuation
        return string

    def removeUpperFromTokenList(self, tokens):
        newList = list()
        for token in tokens:
            newList.append(token.lower())
        return newList

    def convertListToDictionary(self, list):
        dictionary = defaultdict(int)
        for token in list:
            dictionary[token] += 1
        return dictionary

