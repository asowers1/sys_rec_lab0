__author__ = 'andrew'
import MLStripper
import HTMLGetter


print("hello world")

h = HTMLGetter.HTMLGetter()
html = h.getHTMLFromURL("http://theverge.com/")

for line in html:
    print (line)

#def strip_tags(html):
    #s = MLStripper()
    #s.feed(html)
    #return s.get_data()