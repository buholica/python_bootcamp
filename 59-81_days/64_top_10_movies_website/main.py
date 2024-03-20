from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from dotenv import load_dotenv
import os

load_dotenv("C:\\Users\\Oksana\\Desktop\\passwords.env.txt")

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBHO6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

MOVIE_API_TOKEN = os.getenv("MOVIE_API_TOKEN")
MOVIE_API_KEY = os.getenv("MOVIE_API_KEY")
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {MOVIE_API_TOKEN}",
}

# CREATE DB
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies_database.db"
db = SQLAlchemy(app)


# Form for editing a movie rating and reviews
class EditForm(FlaskForm):
    rating = StringField(label='Your Rating Out of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField(label="Your Review", validators=[DataRequired()])
    submit = SubmitField(label="Done")


# Form for adding a new movie
class AddForm(FlaskForm):
    movie_title = StringField(label='Movie Title', validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")


# CREATE TABLE
class Movie(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Book data: ('{self.id}', '{self.title}', '{self.author}', '{self.rating}')"


# with app.app_context():
#     db.create_all()


# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )


# second_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )

# with app.app_context():
#     db.session.add(new_movie)
#     db.session.add(second_movie)
#     db.session.commit()


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie))
    all_movies = result.scalars()
    return render_template("index.html", movies=all_movies)


@app.route("/delete")
def delete():
    """Delete a selected movie"""
    movie_id = request.args.get("id")
    movie_to_delete = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))



@app.route("/edit", methods=["GET", "POST"])
def edit():
    """Edit a selected movie"""
    edit_form = EditForm()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    if edit_form.validate_on_submit():
        movie.rating = float(edit_form.rating.data)
        movie.review = edit_form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form=edit_form, movie=movie)


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    """Add a new movie"""
    add_form = AddForm()
    if add_form.validate_on_submit():
        movie_title = add_form.movie_title.data
        url = f"https://api.themoviedb.org/3/search/movie"
        response = requests.get(url, params={"api_key": MOVIE_API_KEY, "query": movie_title})
        movie_data = response.json()["results"]
        return render_template("select.html", options=movie_data)

    return render_template("add.html", form=add_form)

@app.route("/select", methods=["GET", "POST"])
def add_movie():
    """Select a new movie that will be added to the DB"""
    url = f"https://api.themoviedb.org/3/search/movie"
    response = requests.get(url, params={"api_key": MOVIE_API_KEY, "query": movie_title})
    movie_data = response.json()["results"]
    return redirect(url_for('home'))

    return render_template("select.html")



if __name__ == '__main__':
    app.run(debug=True)
