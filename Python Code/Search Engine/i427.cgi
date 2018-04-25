#! /usr/local/bin/python3

print('Content-type: text/html\n')

import cgi
from webRetrieve import *

html = """
<!doctype html>
<html>
<head><meta charset="UTF-8">
<title>Search Results</title></head>
<body>
<h1><a href="https://cgi.soic.indiana.edu/~spbooth/i427/butler.png"><img style="display: block; margin-left: auto; margin-right: auto;" title="Butler Search Engine Logo" src="https://cgi.soic.indiana.edu/~spbooth/i427/butler.png" alt="" /></a></h1>
<p>Hits: <br /> </p><br />
{}
</body>
</html>"""
form = cgi.FieldStorage() #sets up the form
searchTerms = form.getfirst('query', 'germany') #gets the name of the package with a default to hippo
searchMode = form.getfirst('submit', 'most') #gets the method of the delivery with a default to flying drone
search = searchTerms.split()
search = [str(term) for term in search]
results = retrieve(searchMode, search)
if str(results) == results:
    print(html.format(results))
else:
    results = sorted(results)
    results = results[::-1]
    itemList = ""
    if len(results) > 100:
        for i in range(101):
            itemList += "<a href='"+ str(results[i][1]) +"'>"+ str(results[i][1]) + "</a><br /><br />"
        print(html.format(itemList))
    else:
        for i in range(len(results)):
            itemList += "<a href='"+ str(results[i][1]) +"'>"+ str(results[i][1]) + "</a><br /><br />"
        print(html.format(itemList))
