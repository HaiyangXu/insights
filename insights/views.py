from flask import render_template, flash, redirect
from insights import app,db,models


@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Miguel' }
    posts = [
        { 
            'author': { 'nickname': 'John' }, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': { 'nickname': 'Susan' }, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    feeds=[{'title':item.title,'link':item.link} for item in models.FeedsItem.query.all()]
    return render_template('index.html',
        title = 'Home',
        user = user,
        posts = feeds)

 