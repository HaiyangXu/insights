from flask import render_template, flash, redirect
from insights import app,db,forms
from insights.models import *


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
        for feedsitem,feeds in db.session.query(FeedsItem,Feeds).join(Feeds).all()
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

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = forms.LoginForm()
    return render_template('login.html',
        title = 'Sign In',
        form = form)
        
@app.route('/test')
def test():
    return render_template('test.html')
        
