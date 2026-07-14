from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for
)

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///albums.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Album(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(120),
        nullable=False
    )

    artist = db.Column(
        db.String(120),
        nullable=False
    )

    genre = db.Column(
        db.String(80),
        nullable=False
    )

    year = db.Column(
        db.Integer,
        nullable=False
    )

    stock = db.Column(
        db.Integer,
        nullable=False,
        default="0"
    )

    @property
    def in_stock(self):
        return self.stock > 0

    def __repr__(self):
        return self.id


with app.app_context():
    db.create_all()


@app.route("/")
def index():
    genre = request.args.get("genre", "")

    if genre:
        albums = Album.query.filter_by(
            genre=genre
        ).all()
    else:
        albums = Album.query.all()

    return render_template(
        "index.html",
        albums=albums,
        selected_genre=genre
    )


@app.route(
    "/albums/add",
    methods=["GET", "POST"]
)
def add_album():
    genres = ["Electronic", "Rock", "Hip-Hop", "Experimental"]

    if request.method == "POST":
        clean_title = request.form["title"].title().strip()
        clean_artist = request.form["artist"].strip()
        clean_genre = request.form["genre"].title().strip()
        clean_year = int(request.form["year"])
        clean_stock = int(request.form["stock"])

        album = Album(
            title=clean_title,
            artist=clean_artist,
            genre=clean_genre,
            year=clean_year,
            stock=clean_stock
        )

        db.session.add(album)
        db.session.commit()

        return redirect(
            url_for("index")
        )

    return render_template(
        "add_album.html",
        genres=genres
    )


@app.route(
    "/albums/<int:id>/edit",
    methods=["GET", "POST"]
)
def edit_album(id):
    album = Album.query.get_or_404(id)
    genres = ["Electronic", "Rock", "Hip-Hop", "Experimental"]

    if request.method == "POST":
        clean_title = request.form["title"].title().strip()
        clean_artist = request.form["artist"].strip()
        clean_genre = request.form["genre"].title().strip()
        clean_year = int(request.form["year"])
        clean_stock = int(request.form["stock"])

        album.title = clean_title
        album.artist = clean_artist
        album.genre = clean_genre
        album.year = clean_year
        album.stock = clean_stock

        db.session.commit()

        return redirect(
            url_for(
                "index"
            )
        )

    return render_template(
        "edit_album.html",
        album=album,
        genres=genres
    )


@app.route(
    "/albums/delete/<int:id>")
def delete_album(id):
    album = Album.query.get_or_404(id)

    db.session.delete(album)
    db.session.commit()

    return redirect(
        url_for("index")
    )


if __name__ == "__main__":
    app.run(debug=True)