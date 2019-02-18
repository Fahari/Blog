from flask import render_template
from . import main
from .forms import PostForm,SubscribeForm
from flask_login import login_required
from ..models import Post


# Views
@main.route('/')
# @login_required
def index():

    '''
    View root page function that returns the index page and its data
    '''
    form = SubscribeForm()
    if form.validate_on_submit():
        email = form.email.data
        new_subscriber = Subscriber(email = email)
        db.session.add(new_subscriber)
        db.session.commit()
        # flash("Thank You for subscribing!")
        return redirect(url_for("main.index"))
    post = Post.query.order_by(Post.time.desc())

    message='Hello variable block test'
    title = 'Note Book'
    return render_template("index.html",post = post,form = form,title = title)
