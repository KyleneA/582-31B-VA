from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", title="Welcome", message="Hello from flask templates!")

@app.route("/test")
def test():
    return render_template("test.html", title="Test")


@app.route("/games")
def games():
    games_list = ['Tag', 'Hide & Seek', "Red Light, Green Light"]
    return render_template("games.html", title="Games", games=games_list)

@app.route("/greet")
def greet():
    name = request.args.get("name", "Guest")
    return f"<h1> Hello, {name}! </h1>"

@app.route("/welcome")
def welcome():
    name = request.args.get("name", "Guest")
    program = request.args.get("program", "unknown")
    return f"<h1> {name} studies {program} </h1>"