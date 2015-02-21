# coding:utf-8
import requests
import feedparser

def grabrss(rss_url):
    result = feedparser.parse(rss_url)
    return [{'title':item.title,'link':item.link} for item in result.entries ]




if __name__=='__main__':
    res=grabrss('http://mindhacks.cn/feed/')
    for it in res:
        print it['title']
        print it['link']