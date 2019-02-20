from flask import render_template,redirect,url_for,abort
from . import main
from .forms import PostForm,SubscribeForm,AddComment
from flask_login import login_required,current_user
from ..models import Post,User,Subscriber,Comment
from datetime import datetime
from .. import db
import requests
import json


# Views
@main.route('/',methods= ['POST', 'GET'])
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

    display=requests.get('http://quotes.stormconsultancy.co.uk/random.json').json()
    print(display)
    message='Hello variable block test'
    title = 'Note Book'
    return render_template("index.html",post = post,form = form,title = title,display=display)

@main.route("/add/post/",methods = ["GET","POST"])
@login_required
def add_post():
    form = PostForm()
    title = "Add an article"


    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        posted = str(datetime.now())
        print(posted)
        # if "photo" in request.files:
        #     pic = photos.save(request.files["photo"])
        #     file_path = f"photos/{pic}"
        #     image = file_path
        new_post = Post(title = title, content = content, time = posted)
        new_post.save_post()
        # subscribers = Subscriber.query.all()
        # emails = []
        # for subscriber in subscribers:
        #     emails.append(subscriber.email)
        # for email in emails:
        #     create_mail("Update!","email/update",email, user = current_user)
        # print(emails)
        return redirect(url_for('main.index'))

    return render_template("posts.html",form = form,title = title)

@main.route("/profile/<id>")
def profile(id):
    user = User.query.filter_by(id = id).first()
    posts = Post.query.filter_by(user_id = user.id).order_by(Post.time.desc())
    title = user.username

    if user is None:
        abort(404)
    return render_template("profile/profile.html", user = user,posts = posts, title = title)

@main.route("/comments/<int:id>",methods = ["GET","POST"])
def add_comment(id):
    form = AddComment()
    if form.validate_on_submit():
        name = form.name.data
        content = form.comment.data
        new_comment = Comment(name = name, content = content)
        new_comment.save_comment()
        return redirect(url_for('main.index'))
    comments = Comment.query.all()

    return render_template("comments.html",form = form,comments = comments)

@main.route("/delete/comment/<id>")
def delete_comment(id):
    comment = Comment.query.all()
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for("main.comments"))
