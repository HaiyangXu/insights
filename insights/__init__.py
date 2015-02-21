from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.admin import Admin
app = Flask(__name__)
app.config.from_object('insights.settings')
db = SQLAlchemy(app)
admin = Admin(app)

from insights import views, models
from admin import admin
from RESTful import api
