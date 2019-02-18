from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class PostForm(FlaskForm):

    title = StringField('Post title',validators=[Required()])
    post = TextAreaField('Post', validators=[Required()])
    submit = SubmitField('Submit')

class SubscribeForm(FlaskForm):
    email = StringField("Enter email", validators = [Required()])
    submit = SubmitField("Subscribe")
