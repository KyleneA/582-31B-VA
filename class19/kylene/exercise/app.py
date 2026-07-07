from flask import Flask, request, render_template
from main_routes import main
from movies_routes import movies

app = Flask(__name__)
app.register_blueprint(main)
app.register_blueprint(movies)