from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class PostForm(FlaskForm):

    title = StringField('Post title',validators=[Required()])
    content = TextAreaField('Post', validators=[Required()])
    submit = SubmitField('Submit')

class SubscribeForm(FlaskForm):
    email = StringField("Enter email", validators = [Required()])
    submit = SubmitField("Subscribe")

class AddComment(FlaskForm):
    name = StringField("Name", validators = [Required()])
    comment = TextAreaField("Comment", validators = [Required()])
    submit = SubmitField("Comment")
