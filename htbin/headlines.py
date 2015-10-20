#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
import threading


def googleNews():
    response = requests.get('http://news.google.com/')
    soup = BeautifulSoup(response.content, 'html.parser')
    print "Content-type: text/html"
    print
    print '<div id="google" style="float: left; width: 45%;">'
    print "<h1>Headlines</h1>"
    print soup.find_all('h2', {"class" : "esc-lead-article-title"})
    print "</div>"
    
def twitterTrends():
    response = requests.get('https://twitter.com/whatstrending')
    soup = BeautifulSoup(response.content, 'html.parser')
    print "Content-type: text'html"
    print
    print '<div id="twitter" style="float: right; width: 45%;">'    
    print "<h1>Twitter Trends</h1>"
    print soup.find_all('p', {"class" : "tweet-text"})
    print "</div>"
    
thread1 = threading.Thread(target=googleNews, args=())
thread1.start()

thread2 = threading.Thread(target=twitterTrends, args=())
thread2.start()

