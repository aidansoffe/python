from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension 
from random import randint
app = Flask(__name__)
app.config['SECRET_KEY'] = 'oh so secret'
debug = DebugToolbarExtension(app)

@app.route('/')
def root_page():
  r = """
  <html>
  <body>
  <h1>This is the home page</h1>
  <p>Thanks for visiting</p>
  <a href='/hello'> Go to hello page</a>
  </body>
  </html>
  """
  return r

@app.route('/hello')
def say_hello():
  return render_template("hello.html")

@app.route('/goodbye')
def say_bye():
  return "GOOD BYE MY FRIEND!"

@app.route('/search')
def search():
  term = request.args['term']
  sort = request.args['sort']
  return f"<h1>Search result for term is: {term}</h1> <p> Sorting by: {sort}</p>"


@app.route('/add-comment')
def add_comment_form():
  return """
  <h1>Add a comment</h1>
  <form method='POST'>
  <input type='text' placeholder='comment' name='comment'/>
  <input type='text' placeholder='username' name='username'/>
  <button>Submit</button>
  </form>
  """

@app.route('/add-comment', methods=["POST"] )
def save_comment():
  comment = request.form['comment']
  username = request.form['username']
  print (request.form)
  return f"""
  <h1>Saved comment</h1>
  <ul>
  <li>Username: {username}</li>
  <li>Comment: {comment}</li>
  </ul>
  """


@app.route('/r/<subreddit>')
def show_subreddit(subreddit):
  return f"<h1> Browsing the {subreddit} in Subreddit</h1>"



@app.route('/<subreddit>/comments/<int:post_id>')
def show_comments(subreddit, post_id):
  return f"<h1> Viewing comments for post {post_id} form the {subreddit} Subreddit</h1>"

POSTS ={
  1: "Hello",
  2: "Bye",
  3: "How are you?"
}

@app.route('/post/<int:id>')
def get_id(id):
  post = POSTS.get(id, "post not found") #if nothing found will return post not found message
  return f"<h1> {post}</h1>"


@app.route('/lucky')
def lucky_number():
  num = randint(1, 20)
  return render_template('lucky.html', lucky_num = num, msg = "you are so lucky")


app.route('/form')
def forms():
  return render_template('form.html')