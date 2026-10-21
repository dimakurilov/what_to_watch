from random import randint

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SECRET_KEY'] = 'secret'
db = SQLAlchemy(app)


# Модель
class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    text = db.Column(db.Text, nullable=False)


# Главная
@app.route('/')
def index_view():
    stories = Story.query.all()
    return render_template('stories.html', stories=stories)


# Добавление
@app.route('/add')
def add_view():
    return 'Это страница добавления рассказа'


# Случайный рассказ
@app.route('/story')
def random_story_view():
    stories_count = Story.query.count()
    random_story = Story.query.get_or_404(randint(1, stories_count))
    return render_template('random.html', story=random_story)
