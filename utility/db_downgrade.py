#!flask/bin/python
from migrate.versioning import api
from insights.settings import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO
 
v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
try:
    api.downgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, v - 1)
except Exception, e:
    pass
    
print 'Current database version: ' + str(api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO))
