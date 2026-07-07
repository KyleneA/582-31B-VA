from flask import Blueprint, render_template, request

movies = Blueprint("movies", __name__)

MOVIES = [
    {"title": "Inception", "genre": "Sci-Fi", "year": 2010},
    {"title": "Interstellar", "genre": "Sci-Fi", "year": 2014},
    {"title": "Spirited Away", "genre": "Animation", "year": 2001},
    {"title": "Whiplash", "genre": "Drama", "year": 2014},
    {"title": "Parasite", "genre": "Thriller", "year": 2019}
]

@movies.route("/movies")
def movies_list():
    return render_template("movies.html", movies=MOVIES)


@movies.route("/movie_details")
def movie_details():
    movie_title = request.args.get("movie", "unknown movie")
    
    return render_template("movie_detail.html", movie_title=movie_title, movies=MOVIES)