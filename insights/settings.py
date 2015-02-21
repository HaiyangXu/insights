# only UPPERCASE be export as settings



import os

###################     SQLALCHEMY Settings         ##################
basedir = os.path.abspath(os.path.dirname(__file__))
dbdir=os.path.abspath(os.path.join(basedir,'..','db'))
try:
    os.mkdir(dbdir)
except Exception, e:
    pass
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(dbdir, 'data.db')
SQLALCHEMY_DATABASE_URI ='postgresql://dbfqwmlqiopsfo:OpXfSaGk3mqoqbLz9HRRI9DX0z@ec2-54-204-45-65.compute-1.amazonaws.com:5432/db07o0s1t78g8i'

SQLALCHEMY_MIGRATE_REPO = os.path.join(dbdir, 'db_repository')


CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]
    


