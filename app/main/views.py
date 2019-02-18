from flask import render_template,redirect,url_for
from . import main
from .forms import PostForm,SubscribeForm
from flask_login import login_required,current_user
from ..models import Post,User,Subscriber
from datetime import datetime


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

    message='Hello variable block test'
    title = 'Note Book'
    return render_template("index.html",post = post,form = form,title = title)

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
        subscribers = Subscriber.query.all()
        emails = []
        for subscriber in subscribers:
            emails.append(subscriber.email)
        for email in emails:
            create_mail("Update!","email/update",email, user = current_user)
        print(emails)
        return redirect(url_for('main.index'))

    return render_template("posts.html",form = form,title = title)
