from flask import render_template, redirect, url_for, flash
from . import app, db
from .forms import OpinionForm
from .models import Opinion
from random import choice

@app.route('/')
def index_view():
    opinions = Opinion.query.all()
    return render_template('index.html', opinions=opinions)

@app.route('/add', methods=['GET', 'POST'])
def add_view():
    form = OpinionForm()
    if form.validate_on_submit():
        text = form.text.data
        if Opinion.query.filter_by(text=text).first():
            flash('Такое мнение уже было оставлено ранее!', 'error')
            return render_template('add_opinion.html', form=form)
            
        opinion = Opinion(
            title=form.title.data,
            text=text,
            source=form.source.data
        )
        db.session.add(opinion)
        db.session.commit()
        return redirect(url_for('index_view'))
        
    return render_template('add_opinion.html', form=form)

@app.route('/story')
def random_story_view():
    opinions = Opinion.query.all()
    if not opinions:
        return "В базе пока нет рассказов."
    random_opinion = choice(opinions)
    return render_template('random.html', story=random_opinion)