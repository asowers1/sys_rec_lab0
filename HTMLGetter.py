__author__ = 'andrew'
import urllib.request

class HTMLGetter():
    def __init__(self):
        print ("init")

    def getHTMLFromURL(self, url):
    # Download the file from `url` and save it locally under `file_name`:
        with urllib.request.urlopen(url) as response, open("html.html", 'wb') as out_file:
            data = response.read() # a `bytes` object
            out_file.write(data)

        return open("html.html")
