from flask import Blueprint
movies = Blueprint('movies', __name__)


@movies.route("/movies", methods=['GET'])
def movie_record():
    return "Afra Tafri is funny movie"
