from celery import Celery
import sys
sys.path.append('..')
from insights import models,db
import robot
from datetime import datetime
celery = Celery(__name__)
celery.config_from_object('settings')
#celery = Celery('tasks', broker='amqp://guest@localhost//')



@celery.task
def grabrss(rss_url,feed_id):
    res= robot.grabrss(rss_url)
    for item in res:
        title=item['title']
        link=item['link']
        #feed_id=item['feed_id']
        des=item['des']
        feeditem = models.FeedsItem(title=title,link=link,des=des,feed_id=feed_id,date=datetime.now())
        db.session.add(feeditem)
    try:
        db.session.commit()
    except Exception, e:
        db.session.rollback()
    
@celery.task
def addToQueue():
    for feed in models.Feeds.query.all():
        if feed.rss :
            grabrss.delay(feed.rss,feed.id)


    


#start a addToQueue task once restart
if __name__=='__main__':
    print "start a addToQueue task once restart"
    addToQueue.delay()