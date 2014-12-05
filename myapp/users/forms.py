from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, SubmitField
from wtforms.validators import Required, Length


class LoginForm(Form):
    email = TextField('Email', validators=[Required()])
    password = PasswordField('Password', validators=[Required(), Length(min=5)])
    submit = SubmitField('Submit')

class CreateAccForm(Form):
    username = TextField('Username', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    email = TextField('Email', validators=[Required()])
    submit = SubmitField("Create account")
