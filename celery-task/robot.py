# coding:utf-8
import requests
import feedparser
import re
from datetime import datetime
from insights import models,db

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
    for item in items:
        feeditem = models.FeedsItem(
            title=item.title,
            link=item.link,
            des=striphtml(item.description),
            feed_id=feed_id,
            date=datetime.now()
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