__author__ = 'andrew'

import HTMLGetter
import SoupMachine
from collections import defaultdict
import nltk
import nltk.data
import re
from nltk.stem import *

class Spider():
    html        = None
    soupMachine = None
    mlStriper   = None


    def __init__(self):
        htmlGetter = HTMLGetter.HTMLGetter()
        html = htmlGetter.getHTMLFromURL("http://archive.wired.com/wired/archive/12.10/tail_pr.html")
        self.soupMachine = SoupMachine.SoupMachine(html)
        title = self.soupMachine.getTitle()
        print("Title of Page: " + title)

        strippedhtml = self.removePunc(self.removeComments(self.removeHtmlComments(self.soupMachine.getAllText())))
        tokens = nltk.word_tokenize(strippedhtml)

        print("Number of Tokens: " + str(len(tokens)))

        terms = self.convertListToDictionary(tokens)
        print("Number of Terms: " + str(len(terms)))

        #Lowercase all terms
        self.removeUpperFromObject(tokens)

        lowerTerms = self.convertListToDictionary(tokens)

        print('Number of Terms after lowercase: ' + str(len(lowerTerms)))

        porterTerms = self.convertToPorterTerms(lowerTerms)
        print('Number of Terms after Porter Stemmer: ' + str(len(set(porterTerms))))


    def removeComments(self, string):
        string = re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,string) # remove all occurance streamed comments (/*COMMENT */) from string
        string = re.sub(re.compile("//.*?\n" ) ,"" ,string) # remove all occurance singleline comments (//COMMENT\n ) from string
        return string

    def removeHtmlComments(self, string):
        string = re.sub(re.compile("<!--.*?-->",re.DOTALL ) ,"" ,string) # remove all occurance HTML comments (<!-- -->) from string
        return string

    def removePunc(self, string):
        string = re.sub(re.compile("[^-.\"'\w\s]",re.DOTALL ) ,"" ,string) # remove all occurances punctuation
        return string

    def removeUpperFromObject(self, objects):
        for i in range(len(objects)):
            objects[i] = objects[i].lower()

    def convertListToDictionary(self, list):
        dictionary = defaultdict(int)
        for token in list:
            dictionary[token] += 1
        return dictionary

    def convertToPorterTerms(self, terms):
        porterTerms = []
        for i in terms:
            porterTerms.append(PorterStemmer().stem_word(i))
        return porterTerms