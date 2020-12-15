from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension 
from random import randint, choice, sample
app = Flask(__name__)
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False