from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import Required
class FirePut(Form):
    name = StringField("username",validators=[Required()])
    email = StringField("email",validators=[Required()])
    product = StringField("product name",validators=[Required()])
    phonenumber=StringField("Phone number",validators=[Required()])


