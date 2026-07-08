from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# address to database (browser based)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
# we disable change tracking (following every change made in db) to save memory
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# initializing database
db = SQLAlchemy(app)

# Model of Movies from db data
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(80), nullable=False)

    # optional: give cleaner debugging representation of model in Python
    def __repr__(self):
        return f"<Movie {self.title}>"

# Defining that the model class above DOESN'T automatically create the real database table
# The code below tells Flask-SQLAlchemy to create the tables. 
# (Documentation explains that many extension operations require an application context)
with app.app_context():
    # builds the table  in the db if it doesn't exist
    db.create_all()

@app.route("/")
def index():
    movies = Movie.query.all()
    return render_template("index.html", movies=movies)

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/add", methods=["GET", "POST"])
def add_movie():
    if request.method == "POST":
        # taking data from the form
        title = request.form["title"].capitalize()
        year = int(request.form["year"])
        genre = request.form["genre"].capitalize()

        # create object of Model
        movie = Movie(title=title, year=int(year), genre=genre)

        # add and commit the new entry to the database
        db.session.add(movie)
        db.session.commit()

        # once done, goes to the index page
        return redirect(url_for("index"))
    
    return render_template("add_movie.html")

@app.route("/edit/<int:movie_id>", methods=["GET", "POST"])
def edit_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)

    if request.method == "POST":
        movie.title = request.form["title"].capitalize()
        movie.year = int(request.form["year"])
        movie.genre = request.form["genre"].capitalize()

        db.session.commit()

        return redirect(url_for("index"))

    return render_template("edit_movie.html", movie=movie)

@app.route("/delete/<int:movie_id>")
def delete_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)

    db.session.delete(movie)

    db.session.commit()

    return redirect(url_for("index"))



