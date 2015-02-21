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
        linkv =item['link']
        feed = models.FeedsItem(title=title,link=linkv)
        db.session.add(feed)
        
    db.session.commit()
    
@celery.task
def addTo():
    for feed in models.Feeds.query.all():
        grabrss.delay(feed.url)

@celery.task
def add(x,y):
    print x+y
    return x+y
    
@celery.task
def testschedule(a,b):
    for i in range(100):
        addTo.delay()

if __name__=='__main__':
    pass