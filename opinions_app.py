from random import randint

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# noqa: E302
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SECRET_KEY'] = 'secret'
db = SQLAlchemy(app)

# noqa: E302
class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    text = db.Column(db.Text, nullable=False)

# noqa: E302
@app.route('/')
def index_view():
    stories = Story.query.all()
    return render_template('stories.html', stories=stories)

# noqa: E302
@app.route('/add')
def add_view():
    return 'Это страница добавления рассказа'

# noqa: E302
@app.route('/story')
def random_story_view():
    stories_count = Story.query.count()
    random_story = Story.query.get_or_404(randint(1, stories_count))
    return render_template('random.html', story=random_story)
# конец файла (обязательно нажмите Enter здесь)