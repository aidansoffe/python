from flask import Flask, request
app = Flask(__name__)

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
  html = """
  <html>
  <body>
  <h1>Hi there</h1>
  <p> how are you?</p>
  </body>
  </html>
  """
  return html

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



@app.route('/<subreddit>/comment/<int:post_id>')
def show_comments(subreddit, post_id):
  return f"{post_id}{subreddit}"

POSTS ={
  1: "Hello",
  2: "Bye",
  3: "How are you?"
}

@app.route('/post/<int:id>')
def get_id(id):
  post = POSTS.get(id, "post not found") #if nothing found will return post not found message
  return f"<h1> {post}</h1>"

