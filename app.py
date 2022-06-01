from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_worlddsds():
    return "<p>Hello, World! this the landing page ola</p>"

@app.route("/about")
def about_controller():
    return "<p>Hi, this an about page, hey hey</p>"

@app.route("/name/<name>")
def hello(name):
    return f"Hello, my name is {escape(name)}!"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id} is a numeric value'