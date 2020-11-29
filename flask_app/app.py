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
  <input type='text' placeholder='comment'/>
  <button>Submit</button>
  </form>
  """

@app.route('/add-comment', methods=["POST"] )
def save_comment():
  return """
  <h1>Saved comment</h1>
  """