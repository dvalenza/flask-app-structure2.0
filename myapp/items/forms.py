from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, FileField
from wtforms.validators import Required, Length

class CreateNewItemForm(Form):
    name = TextField('Name', validators=[Required()])
    description = TextAreaField('Description', validators=[Required()])
    quantity = TextField('Quantity')
    file = FileField()
    submit = SubmitField("Submit")
