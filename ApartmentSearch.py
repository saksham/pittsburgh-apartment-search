import datetime
import mechanize, re
from visited import *
from exploration import *

#parameters
keywords=["shadyside", "squirrel hill", "oakland", "greenfield", "friendship", "southside", ""]
modes=['sub', 'apa']
min="400"
max="700"
postedSince= datetime.datetime(2013, 8, 1)

# Get a list of items browsed so far
bi = BrowsedItems()
# Explore new apartments
ApartmentsExplorer.start_html()
new_cnt = 0
ApartmentsExplorer.write_html("<div class='row'>")
for mode in modes:
    ApartmentsExplorer.write_html("<div id='"+mode+"' class='span6'><h1>"+mode+"</h1>")
    for keyword in keywords:
        exp = ApartmentsExplorer(keyword, min, max, bi.visited, mode, postedSince)
        new_cnt += len(exp.ids)
        exp.write_item_links()
    ApartmentsExplorer.write_html("</div>")
ApartmentsExplorer.write_html("</div>")
ApartmentsExplorer.write_html("<div class='row'><h2>Old: " + str(len(bi.visited)) + ", New: " + str(new_cnt) + "</h2></div>")
ApartmentsExplorer.end_html()
