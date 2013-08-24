import mechanize, re, os,urllib
import json
import datetime

class ApartmentsExplorer(object):
    __dir, __src = os.path.split(os.path.abspath(__file__))
    __temp_html = __dir + "/Temp.html"

    def __init__(self, keyword, min, max, visited, mode, postedSince):
        # Construct the URL for RSS feed
        self.keyword = keyword
        self.mode = mode
        self.url="http://pittsburgh.craigslist.org/jsonsearch/"+self.mode+"?bedrooms=1&useMap=1&format=rss"
        if max != None and len(max.strip()) > 0:
            self.url = self.url+"&maxAsk="+max
        if min != None and len(min.strip()) > 0:
            self.url = self.url+"&minAsk="+min
        if keyword != None and len(keyword.strip()) > 0:
            self.url = self.url+"&srchType=A&query="+urllib.quote_plus(keyword)

        # Fire up a browser using mechanize
        browser = mechanize.Browser()
        browser.set_handle_robots(False)

        # Browse to the RSS page to collect IDs
        json_data = browser.open(self.url).read()
        self.data = json.loads(json_data)
        self.ids = {}
        for posting in self.data[0]:
            posting_id = posting[u'PostingID']
            if posting_id not in visited and u'PostingURL' in posting:
                postedOn = datetime.datetime.fromtimestamp(long(posting[u'PostedDate']))
                if postedOn >= postedSince:
                    url = posting[u'PostingURL']
                    title = posting[u'PostingTitle']
                    self.ids[posting_id] = (url, title)

    @staticmethod
    def start_html():
        html = open(ApartmentsExplorer.__temp_html, "w")
        html.write("<html>\n<head>\n")
        html.write("<link rel='stylesheet' type='text/css' href='css/bootstrap.css'/>\n")
        html.write("<link rel='stylesheet' type='text/css' href='css/site.css'/>\n")
        html.write("<script type='text/javascript' src='js/bootstrap.js'></script>\n")
        html.write("</head>\n<body>\n<div class='container'>\n")

    def write_item_links(self):
        html = open(ApartmentsExplorer.__temp_html, "a")
        html.write("<h2>'"+self.keyword+"': " + str(len(self.ids)) + "</h2>\n<ul>")
        for id in self.ids:
            print self.ids[id]
            html.write("<li><a href='http:"+self.ids[id][0]+"'>"+id+"</a>," + self.ids[id][1] + "</li>\n")
        html.write("</ul>")

    @staticmethod
    def write_html(html_src):
        html = open(ApartmentsExplorer.__temp_html, "a")
        html.write(html_src)

    @staticmethod
    def end_html():
        html = open(ApartmentsExplorer.__temp_html, "a")
        ApartmentsExplorer.write_html("</div></body></html>")

