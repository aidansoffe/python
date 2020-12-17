from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension 
from random import randint, choice, sample
app = Flask(__name__)
app.config['SECRET_KEY'] = 'oh so secret'
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


responses = []

""" Create a route for a single question"""

@app.route('/question')
def ask_question():
  return render_template('questions.html')