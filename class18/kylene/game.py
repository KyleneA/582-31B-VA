from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<a type='button' style='padding: 10px; background-color: honeydew; border: 1px solid forestgreen; margin-right: 30px;' href='/games'> games </a> <a type='button' style='padding: 10px; background-color: honeydew; border: 1px solid forestgreen;' href='/students'> students </a> <h1>Home</h1>"

@app.route("/games")
def games():
    return "<a type='button' style='padding: 10px; background-color: honeydew; border: 1px solid forestgreen; margin-right: 30px;' href='/'> home </a> <a type='button' style='padding: 10px; background-color: honeydew; border: 1px solid forestgreen;' href='/students'> students </a> <h1>Games</h1> <ul> <li>hide and seek</li> <li>tag</li> <li>red light, green light</li> </ul>"

@app.route("/students")
def students():
    return "<a type='button' style='padding: 10px; background-color: honeydew; border: 1px solid forestgreen; margin-right: 30px;' href='/'> home </a> <a type='button' style='padding: 10px; background-color: honeydew; border: 1px solid forestgreen;' href='/games'> games </a> <h1>Students</h1>"