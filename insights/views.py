from flask import render_template, flash, redirect
from insights import app,db,models,forms


@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Miguel' }
    feeds=[{'title':item.title,'link':item.link} for item in models.FeedsItem.query.all()]
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
            flash("Exception !")
            
    return render_template('addfeeds.html',
        form= form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = forms.LoginForm()
    return render_template('login.html',
        title = 'Sign In',
        form = form)