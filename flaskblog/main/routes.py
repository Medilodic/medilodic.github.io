from flask import render_template, request, Blueprint
from flaskblog.models import Post

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('index.html', posts=posts)


@main.route("/about")
def about():
    project_name = "My Blog/Social Media Project"
    project_description = "Welcome to my blog/social media project! This is a platform where users can share their thoughts, connect with others, and discover interesting content. Join our community today!"
    founder_names = ["Medilodic"]
    year_founded = 2023

    return render_template('about.html', title='About',
                           project_name=project_name,
                           project_description=project_description,
                           founder_names=founder_names,
                           year_founded=year_founded)