from flask import Flask, render_template, url_for, request
from recommender_engine import get_recommendations
import os

app = Flask(__name__)

@app.route('/')
@app.route('/home', methods = ["GET", "POST"])
def home():
	return render_template("home.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/result', methods = ["GET", "POST"])
def result():
	if request.method == "POST":
		movie_name = request.form["movie_name"]

	else:
		movie_name = request.args.get("movie_name")

	recommended_movies = get_recommendations(movie_name, 5)

	return render_template("result.html", given_movie = movie_name, movies = recommended_movies)


if __name__ == "__main__":
	app.run(debug = True, host='0.0.0.0', port = 5001)