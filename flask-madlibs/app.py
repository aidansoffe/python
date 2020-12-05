from flask import Flask, render_template, request, redirect
from stories import *

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
  if request.method == "POST":
    req = request.form
    return  story.generate({"place":req["place"], "noun": req["noun"], "verb":req["verb"], "adjective":req["adj"], "plural_noun": req["plural_noun"]})
 
f"<h1>Your Story</h1>"