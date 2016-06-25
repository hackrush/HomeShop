from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired
class FirePut(Form):
    name = StringField("username", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired()])
    product = StringField("product name", validators=[DataRequired()])
    phonenumber=StringField("Phone number",validators=[DataRequired()])

