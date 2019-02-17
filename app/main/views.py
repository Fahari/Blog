from flask import render_template
from . import main
from .posts import PostForm


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    message='Hello variable block test'
    title = 'Note Book'
    return render_template('index.html',message=message,title=title)
