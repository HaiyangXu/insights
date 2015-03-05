from celery import Celery
import sys
sys.path.append('..')

import robot

celery = Celery(__name__)
celery.config_from_object('settings')
#celery = Celery('tasks', broker='amqp://guest@localhost//')



@celery.task
def grabrss(rss_url,feed_id):
    return robot.grabrss(rss_url,feed_id)
    
@celery.task
def addToQueue():
    feeds=robot.getFeeds()
    for feed in feeds:
        grabrss.delay(feed.rss,feed.id)


    


#start a addToQueue task once restart
if __name__=='__main__':
    print "start a addToQueue task once restart"
    addToQueue.delay()