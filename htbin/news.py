#!/usr/bin/env python

import requests

print "Content-type: text/html"
print
print "<h1>News</h1>"
response = requests.get('http://news.google.com/')
print "<p>"
print (response.content)
print "</p>"
