from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required

class LoginForm(Form):
    openid = TextField('openid', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)
    

class AddFeensForm(Form):
    url=TextField('url',validators =[Required()])
    title=TextField('title',validators=[Required()])
    rss=TextField('rss')
    
    
    
