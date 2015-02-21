from insights import app,db,models
from flask.ext.restless import APIManager

manager = APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(models.User, methods=['GET', 'POST'])
manager.create_api(models.Feeds, methods=['GET', 'POST'])
manager.create_api(models.FeedsItem, methods=['GET', 'POST'])