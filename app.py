from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__,static_folder="static")
    

@app.route("/")
def hello():
    return render_template('pages/index.html')
    # return "<p>Hello, World! this the landing page ola</p>"

@app.route("/about")
def about_controller():
    return "<p>Hi, this an about page, hey hey</p>"

@app.route('/projects/')
def projects():
    # https://gco.iarc.fr/data/recent_pub.json
    return render_template('pages/projects.html')

@app.route("/name/<name>")
def name_controller(name):
    return render_template('pages/name.html',name=name)
    # return f"Hello, my name is {escape(name)}!"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return render_template('pages/post.html',post_id=post_id)
    #return f'Post {post_id} is a numeric value'

@app.route("/routes/")
def routes():
    routes = []
    for rule in app.url_map.iter_rules():
        routes.append(rule)

    return render_template('pages/routes.html',routes=routes)

@app.route('/login', methods=['GET', 'POST'])

def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

# to checked: solution to redirect routes to one singe subfolder application for example
with app.test_request_context():
    # print(url_for('/'))
    print(url_for('about_controller'))
    # print(url_for('name_controller', next='/na'))
    print(url_for('name_controller', name='John Doe'))

def show_the_login_form(): 
    return render_template('pages/login.html')
    # return "<p>Login form <br> <input type='text' name='login' placeholder='Enter login'><input type='submit' name='submit' text='Submit'></p>"

def do_the_login():
    if valid_login(request.form['username'],request.form['password']):
        return log_the_user_in(request.form['username'])
    else:
        error = 'Invalid username/password'

    return render_template('pages/login.html',error=error)
    # print("Login form has been submitted")

def log_the_user_in( username ):
    return render_template('pages/account.html',error=error)

def valid_login( login ) : 
    return true 

app.run(host='0.0.0.0', port=5002,debug=True)