#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
response = requests.get('http://news.google.com/')
soup = BeautifulSoup(response.content, 'html.parser')

print "Content-type: text/html"
print
print "<h1>Headlines</h1>"
print soup.find_all('h2', {"class" : "esc-lead-article-title"})

#<h2 class="esc-lead-article-title"></h2>
