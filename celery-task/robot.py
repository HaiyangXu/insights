# coding:utf-8
import requests
import feedparser
import re
from datetime import datetime
from insights import models,db
from HTMLParser import HTMLParser
from time import mktime
description_size=200

def striphtml(data):
    p = re.compile(r'<.*?>')
    plain= p.sub('', data.strip())
    
    if len(plain) <= description_size:
        return plain
    else:
        return plain[:description_size]
    
def grabrss(rss_url,feed_id):
    feed_data = feedparser.parse(rss_url)
    channel,items =feed_data.feed,feed_data.entries
    count=0
    html_parser = HTMLParser()
    def gettime(parsed):
        return datetime.fromtimestamp(mktime(parsed))
    for item in items:
        global date
        if hasattr(item,'published_parsed'):
            date=gettime(item.published_parsed)
        elif hasattr(item,'updated_parsed'):
            date=gettime(item.updated_parsed)
        elif hasattr(item,'created_parsed'):
            date=gettime(item.created_parsed)
        
        feeditem = models.FeedsItem(
            title=html_parser.unescape(item.title),
            link=item.link,
            des=html_parser.unescape(striphtml(item.description)),
            feed_id=feed_id,
            date=date
            )
        db.session.add(feeditem)
        try:
            db.session.commit()
            count=count+1
        except Exception, e:
            db.session.rollback()
            
    return count
            
   


def getFeeds():
    return models.Feeds.query.all()


if __name__=='__main__':
    pass