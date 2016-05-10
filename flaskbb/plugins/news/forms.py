from flask.ext.wtf import Form
from wtforms import TextAreaField
from wtforms.validators import DataRequired

class AddForm(Form):
    name = TextAreaField('name', validators=[DataRequired()])
    text = TextAreaField('text', validators=[DataRequired()])

class DeleteForm(Form):
    name = TextAreaField('name', validators=[DataRequired()])
    
