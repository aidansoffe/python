from flask import Flask, request, render_template, redirect, session
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = '123abc'
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

@app.route('/')
def index():
  #count how many times homepage was visited
  session['count'] = session.get('count', 0) + 1
  return render_template("index.html")

@app.route('/favcolor', methods=['GET','POST'])
def fav_color():
    #choose fav color
    fcolor = request.values.get('color')
    return render_template('color.html', fcolor=fcolor)


@app.route('/redirectme')
def redirect_me():
  #return to a homepage
  return redirect('/')


