from insights import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    website = db.Column(db.String(200))

    def __repr__(self):
        return '<User %r>' % self.username
        
class Feeds(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Unicode(200))
    url = db.Column(db.String(200), unique=True)
    rss = db.Column(db.String(200))
    date = db.Column(db.Date)

    def __repr__(self):
        return '<Title %r>' % self.title
        
class FeedsItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title= db.Column(db.Unicode(200))
    link = db.Column(db.String(200), unique=True)
    des = db.Column(db.Unicode)
    date = db.Column(db.Date)
    hits = db.Column(db.Integer)
        
    def __repr__(self):
        return '<Title %r>' %self.title
