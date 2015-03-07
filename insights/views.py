from flask import render_template, flash, redirect, request ,url_for
from insights import app,db,forms,models
from insights.models import *
import feedparser

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Miguel' }
    feeds=[
        {
            'title':feedsitem.title,
            'link':feedsitem.link,
            'descriptions':feedsitem.des ,
            'date':feedsitem.date,
            'hits':feedsitem.hits,
            'author':feeds.title,
            
        }
        for feedsitem,feeds in db.session.query(FeedsItem,Feeds).join(Feeds).order_by(FeedsItem.date.desc()).all()
        ]
    return render_template('index.html',
        title = 'Home',
        user = user,
        posts = feeds)
        
        
        
@app.route('/addfeeds',methods = ['GET', 'POST'])
def addfeeds():
    form=forms.AddFeensForm()
    if form.validate_on_submit():
        feed=models.Feeds()
        feed.title=form.title.data
        feed.url=form.url.data
        feed.rss=form.rss.data
        db.session.add(feed)
        try:
            db.session.commit()
            flash('Add feeds Successed!  Title=' + form.title.data + ', Url=' + form.url.data)
        except Exception, e:
            db.session.rollback()
            flash("Exception !")
            
    return render_template('addfeeds.html',
        form= form)

@app.route('/addrss')
def addrss():
    rss = request.args.get('url')
    feed_data = feedparser.parse(rss)
    channel, items = feed_data.feed, feed_data.entries
    
    
    if hasattr(channel,'link') and channel.link:
        feed=models.Feeds()
        feed.title=channel.title
        feed.url=channel.link
        feed.rss=rss
        db.session.add(feed)
        try:
            db.session.commit()
            flash('Add feeds Successed!  Title=' + channel.title + ', Url=' + channel.link)
        except Exception, e:
            db.session.rollback()
            flash('Exception ! Title=' + channel.title + ', Url=' + channel.link)
    else:
        flash('Exception ! cannot get '+rss)
    
    return redirect(url_for('index'))

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = forms.LoginForm()
    return render_template('login.html',
        title = 'Sign In',
        form = form)
        
@app.route('/test')
def test():
    return render_template('test.html')
        
