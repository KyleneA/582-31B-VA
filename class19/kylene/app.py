from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> Hello! </h1>"