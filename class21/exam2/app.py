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
    if request.method == "POST":
        clean_title = request.form["title"].title().strip()
        clean_artist = request.form["artist"].capitalize().strip()
        clean_genre = request.form["genre"].capitalize().strip()
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

        print("submitted", clean_title)

        return redirect(
            url_for("index")
        )

    return render_template(
        "add_album.html"
    )


@app.route(
    "/albums/<int:album_id>/edit",
    methods=["GET", "POST"]
)
def edit_album(album_id):
    album = Album.query.get_or_404(album_id)

    if request.method == "POST":
        album.title = request.form["title"]
        album.band = request.form["artist"]
        album.genre = request.form["genre"]
        album.year = request.form["year"]
        album.stock = request.form["amount"]

        return redirect(
            url_for(
                "edit_album",
                id=album.id
            )
        )

    return render_template(
        "add_album.html",
        album=album
    )


@app.route(
    "/albums/<int:album_id>/delete",
    methods=["GET"]
)
def delete_album(album_id):
    album = Album.query.get_or_404(album_id)

    db.session.delete(album)

    return redirect(
        url_for("index")
    )


if __name__ == "__main__":
    app.run(debug=True)