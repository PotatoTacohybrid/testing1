from flask import Flask, render_template
import datetime


app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now()

    return render_template("index.html", now=now)
