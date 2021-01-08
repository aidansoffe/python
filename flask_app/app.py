from flask import Flask, request, render_template, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension 
from random import randint, choice, sample
app = Flask(__name__)
app.config['SECRET_KEY'] = 'oh so secret'
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

@app.after_request
def add_header(req):
    """Add non-caching headers on every request."""
    req.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    req.headers["Pragma"] = "no-cache"
    req.headers["Expires"] = "0"
    req.headers["Cache-Control"] = "public, max-age=0"
    return req

MOVIES = {'Kate', 'Titanic', 'Escape'}

@app.route('/')
def root_page():
  return render_template('home.html')


@app.route('/old-home-page')
def redirect_home():
  """ Redirects to a new home page"""
  flash("That page has moved, This is our new home page!")
  return redirect("/")


@app.route("/movies")
def show_all_movies():
  """ Show all lists of movies"""
  return render_template("movies.html", movies=MOVIES)

@app.route("/movies/json")
def get_movies_json():
  return jsonify(list(MOVIES))

@app.route("/movies/new", methods=['GET','POST'])
def add_movie():
  title = request.form['title']
  if title in MOVIES:
      flash('Movie already exists!', 'error')
  else:
      MOVIES.add(title)
      flash('You added a movie', 'success')
  return redirect('/movies')























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
  num = randint(1, 10)
  return render_template('lucky.html', lucky_num = num, msg = "you are so lucky")

#to choose a random adj import choice
COMPLIMENTS = ['pretty', 'bright', 'delicate', 'irritated']


@app.route('/form')
def forms():
  return render_template("form.html")


@app.route('/form2')
def form2():
  return render_template("form2.html")



@app.route('/greet')
def get_greeting():
  username = request.args["username"]
  nice_thing = choice(COMPLIMENTS)
  return render_template("greet.html", user = username, compliment=nice_thing)


@app.route('/greet2')
def get_greeting2():
  username = request.args["username"]
  wants = request.args.get("wants_compliments")
  nice_things = sample(COMPLIMENTS, 3)
  return render_template("greet2.html", username=username, compliments=wants, nice_things=nice_things)


@app.route('/spell/<word>')
def spell_word(word):
  return render_template("spelling.html", word=word)
