from celery import Celery
import sys
sys.path.append('..')
from insights import models,db
import robot
celery = Celery(__name__)
celery.config_from_object('settings')
#celery = Celery('tasks', broker='amqp://guest@localhost//')



@celery.task
def grabrss(rss_url):
    res= robot.grabrss(rss_url)
    for item in res:
        title=item['title']
        link=item['link']
        feeditem = models.FeedsItem(title=title,link=link)
        db.session.add(feeditem)
    try:
        db.session.commit()
    except Exception, e:
        db.session.rollback()
    
@celery.task
def addToQueue():
    for feed in models.Feeds.query.all():
        if feed.rss :
            grabrss.delay(feed.rss)

@celery.task
def add(x,y):
    print x+y
    return x+y
    

if __name__=='__main__':
    pass