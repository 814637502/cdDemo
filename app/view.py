__author__ = 'sunyawei'

# from flask import Flask
from flask import render_template
from app import app


@app.route("/")
def index():
    print "app"
    return render_template("index.xml")

