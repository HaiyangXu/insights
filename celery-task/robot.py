# coding:utf-8
import requests
import feedparser
import re

description_size=200

def striphtml(data):
    p = re.compile(r'<.*?>')
    plain= p.sub('', data.strip())
    
    if len(plain) <= description_size:
        return plain
    else:
        return plain[:description_size]
    
def grabrss(rss_url):
    result = feedparser.parse(rss_url)
    return [
        {'title':item.title,'link':item.link ,'des':striphtml(item.description)}
        for item in result.entries 
        ]




if __name__=='__main__':
    res=grabrss('http://mindhacks.cn/feed/')
    for it in res:
        print it['title']
        print it['link']