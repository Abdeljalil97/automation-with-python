import feedparser
import delorean
import requests
import datetime

rss = feedparser.parse('http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml')
print(rss.feed.title)