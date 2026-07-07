from flask import Flask
from main_routes import main
from team_routes import teams

app = Flask(__name__)
app.register_blueprint(main)
app.register_blueprint(teams)
