from insights import admin
from insights import models,db
from flask.ext.admin.contrib import sqla
from flask.ext.admin import expose

# required for creating custom filters
from flask.ext.admin.contrib.sqla.filters import BaseSQLAFilter, FilterEqual
# Add custom filter and standard FilterEqual to ModelView
class UserAdmin(sqla.ModelView):
    # each filter in the list is a filter operation (equals, not equals, etc)
    # filters with the same name will appear as operations under the same filter
    column_filters = [
        FilterEqual(models.User.username, 'User Name'), 
    ]
    
class FeedsAdmin(sqla.ModelView):
    # each filter in the list is a filter operation (equals, not equals, etc)
    # filters with the same name will appear as operations under the same filter
    column_filters = [
        FilterEqual(models.User.username, 'User Name'), 
    ]
    
admin.add_view(UserAdmin(models.User, db.session))
admin.add_view(sqla.ModelView(models.Feeds,db.session))
admin.add_view(sqla.ModelView(models.FeedsItem,db.session))
