import os

from flask import Flask, jsonify, abort, request
from flask_cors import CORS, cross_origin
from auth.auth import AuthError, requires_auth
from models import db, Actor, Movie, setup_db


# ----------------------------------------------------------------------------#
# Create and configure the app
# ----------------------------------------------------------------------------#
def create_app(db_path='', test_config=None):
    app = Flask(__name__)
    if db_path:
        setup_db(app, db_path)
    else:
        setup_db(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers",
            "Content-Type, Authorization, true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods",
            "GET, POST, PATCH, DELETE, OPTIONS"
        )
        return response

    # ------------------------------------------------------------------------#
    # Routes
    # ------------------------------------------------------------------------#

    @app.route("/")
    @cross_origin()
    def index():
        return "Home page"

    @app.route("/movies")
    @requires_auth("get:movies")
    def get_movies(payload):
        try:
            movies = Movie.query.all()

            if not movies:
                abort(404)

            movies_list = [i.get_details() for i in movies]

            return jsonify({
                "success": True,
                "movies": movies_list
            })
        except Exception as err:
            if getattr(err, 'code', None) == 404:
                abort(404)
            else:
                print(err)

    @app.route('/movies/<int:movie_id>')
    @requires_auth("get:movies-detail")
    def get_movie_info(payload, movie_id):
        try:
            # movie = Movie.query.get(movie_id)
            movie = db.session.get(Movie, movie_id)
            if not movie:
                abort(404)

            return jsonify({
                "success": True,
                "movie_info": movie.get_details()
            }), 200
        except Exception as err:
            if getattr(err, 'code', None) == 404:
                abort(404)
            else:
                print(err)

    @app.route("/movies", methods=["POST"])
    @requires_auth("post:movies")
    def create_movie(payload):
        try:
            body = request.get_json()
            title = body.get("title", None)
            release_date = body.get("release_date", None)

            if not all((title, release_date)):
                abort(400)

            movie = Movie(
                title=title,
                release_date=release_date
            )
            movie.insert()

            return jsonify({
                "success": True,
                "movie": movie.get_details()
            }), 200

        except Exception as err:
            if getattr(err, 'code', None) == 400:
                abort(400)
            else:
                print(err)

    @app.route("/movies/<int:movie_id>", methods=["PATCH"])
    @requires_auth("patch:movies")
    def edit_movie(payload, movie_id):
        try:
            movie = Movie.query.filter_by(id=movie_id).first()

            if not movie:
                abort(404)

            body = request.get_json()
            title = body.get("title", None)
            release_date = body.get("release_date", None)

            if title:
                movie.title = title
            if release_date:
                movie.release_date = release_date
            movie.update()

            return jsonify({
                "success": True,
                "movie": movie.get_details()
            }), 200

        except Exception as err:
            if getattr(err, 'code', None) == 404:
                abort(404)
            else:
                print(err)

    @app.route("/movies/<int:movie_id>", methods=["DELETE"])
    @requires_auth("delete:movies")
    def delete_movie(payload, movie_id):
        try:
            movie = db.session.get(Movie, movie_id)

            if not movie:
                abort(422)

            movie.delete()

            return jsonify({
                "success": True,
                "deleted": movie.id
            }), 200

        except Exception as err:
            if getattr(err, 'code', None) == 422:
                abort(422)
            else:
                print(err)

    # ------------------------------------------------------------------------#

    @app.route("/actors")
    @requires_auth("get:actors")
    def get_actors(payload):
        try:
            actors = Actor.query.all()

            if not actors:
                abort(404)

            actors_list = [i.get_details() for i in actors]

            return jsonify({
                "success": True,
                "actors": actors_list
            })
        except Exception as err:
            if getattr(err, 'code', None) == 404:
                abort(404)
            else:
                print(err)

    @app.route('/actors/<int:actor_id>')
    @requires_auth("get:actors-detail")
    def get_actor_info(payload, actor_id):
        try:
            actor = db.session.get(Actor, actor_id)

            if not actor:
                abort(404)

            return jsonify({
                "success": True,
                "actor_info": actor.get_details()
            }), 200
        except Exception as err:
            if getattr(err, 'code', None) == 404:
                abort(404)
            else:
                print(err)

    @app.route("/actors", methods=["POST"])
    @requires_auth("post:actors")
    def create_actor(payload):
        try:
            body = request.get_json()
            name = body.get("name", None)
            age = body.get("age", None)
            gender = body.get("gender", None)

            if not all((name, age, gender)):
                abort(400)

            actor = Actor(
                name=name,
                age=age,
                gender=gender
            )
            actor.insert()

            return jsonify({
                "success": True,
                "actor": actor.get_details()
            }), 200

        except Exception as err:
            if getattr(err, 'code', None) == 400:
                abort(400)
            else:
                print(err)

    @app.route("/actors/<int:actor_id>", methods=["PATCH"])
    @requires_auth("patch:actors")
    def edit_actor(payload, actor_id):
        try:
            actor = Actor.query.filter_by(id=actor_id).first()

            if not actor:
                abort(404)

            body = request.get_json()
            name = body.get("name", None)
            age = body.get("age", None)
            gender = body.get("gender", None)

            if name:
                actor.name = name
            if age:
                actor.age = age
            if gender:
                actor.gender = gender

            actor.update()

            return jsonify({
                "success": True,
                "actor": actor.get_details()
            }), 200

        except Exception as err:
            if getattr(err, 'code', None) == 404:
                abort(404)
            else:
                print(err)

    @app.route("/actors/<int:actor_id>", methods=["DELETE"])
    @requires_auth("delete:actors")
    def delete_actor(payload, actor_id):
        try:
            actor = db.session.get(Actor, actor_id)

            if not actor:
                abort(422)

            actor.delete()

            return jsonify({
                "success": True,
                "deleted": actor.id
            }), 200

        except Exception as err:
            if getattr(err, 'code', None) == 422:
                abort(422)
            else:
                print(err)

    # ------------------------------------------------------------------------#
    # Error handling
    # ------------------------------------------------------------------------#

    @app.errorhandler(AuthError)
    def handle_auth_error(ex):
        response = jsonify(ex.error)
        response.status_code = ex.status_code
        return response

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(400)
    def resource_not_found(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    # ------------------------------------------------------------------------#
    # Launch App
    # ------------------------------------------------------------------------#
    return app


app = create_app()
if __name__ == '__main__':
    app.run(debug=False)
