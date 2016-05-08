from flask.ext.wtf import Form
from wtforms import TextAreaField
from wtforms.validators import DataRequired

class AddForm(Form):
    text = TextAreaField('text', validators=[DataRequired()])
