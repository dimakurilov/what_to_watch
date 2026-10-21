from random import randint
from flask import Flask, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SECRET_KEY'] = 'my_secret_key'
db = SQLAlchemy(app)


class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    text = db.Column(db.Text, nullable=False)


@app.route('/')
def index_view():
    stories = Story.query.all()
    return render_template('stories.html', stories=stories)


@app.route('/add')
def add_view():
    return 'Это страница добавления рассказа'


@app.route('/story')
def random_story_view():
    stories_count = Story.query.count()
    random_story = Story.query.get_or_404(
        randint(1, stories_count)
    )
    return render_template('random.html', story=random_story)