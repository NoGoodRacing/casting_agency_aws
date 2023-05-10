import os
from dotenv import load_dotenv

from flask_sqlalchemy import SQLAlchemy

load_dotenv()

DATABASE_URI = os.getenv('DATABASE_URI')
db = SQLAlchemy()


def setup_db(app, database_path=DATABASE_URI):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    with app.app_context():
        db.create_all()


movie_actor = db.Table(
    "movie_actor",
    db.Column("movie_id", db.ForeignKey("movies.id")),
    db.Column("actor_id", db.ForeignKey("actors.id"))
)


class Movie(db.Model):
    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    release_date = db.Column(db.Integer, nullable=False)
    actors = db.relationship(
        "Actor",
        secondary="movie_actor",
        back_populates="movies"
    )

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def get_details(self):
        return {
            "id": self.id,
            "title": self.title,
            "release_date": self.release_date,
        }

    def __repr__(self):
        return f"Movie: {self.title} ({str(self.release_date)})"


class Actor(db.Model):
    __tablename__ = "actors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    age = db.Column(db.Integer(), nullable=False)
    gender = db.Column(db.String(120), nullable=False)
    movies = db.relationship(
        "Movie",
        secondary="movie_actor",
        back_populates="actors"
    )

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def get_details(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender
        }

    def __repr__(self):
        return f"Actor: {self.name}"
