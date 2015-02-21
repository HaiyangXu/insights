#!flask/bin/python
from migrate.versioning import api
from insights.settings import SQLALCHEMY_DATABASE_URI
from insights.settings import SQLALCHEMY_MIGRATE_REPO
from insights import db
import os.path
db.create_all()
if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
    api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
    print('Create db:{0} \nVersion:{1}'.format(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REPO))

else:
    try:
        api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
    except Exception, e:
        print('')
        pass
    print('Existed db:{0} \nVersion:{1}'.format(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REPO))
