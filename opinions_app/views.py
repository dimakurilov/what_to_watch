from flask import redirect, url_for, flash
from . import app, db
from .forms import OpinionForm
from .models import Opinion
from random import choice

@app.route('/')
def index_view():
    opinions = Opinion.query.all()
    if not opinions:
        return "<h1>Пока нет ни одного мнения.</h1><a href='/add'>Добавить</a>"
        
    html = "<h1>Мнения о фильмах</h1><a href='/add'>Добавить мнение</a><hr>"
    for opinion in opinions:
        html += f"<div style='border:1px solid #ccc; margin:10px; padding:10px;'>"
        html += f"<h3>{opinion.title}</h3>"
        html += f"<p>{opinion.text}</p>"
        html += f"</div>"
    return html

@app.route('/add', methods=['GET', 'POST'])
def add_view():
    form = OpinionForm()
    if form.validate_on_submit():
        text = form.text.data
        if Opinion.query.filter_by(text=text).first():
            flash('Такое мнение уже было оставлено ранее!', 'error')
            return "Такое мнение уже есть. <a href='/add'>Назад</a>"
            
        opinion = Opinion(
            title=form.title.data,
            text=text,
            source=form.source.data
        )
        db.session.add(opinion)
        db.session.commit()
        return redirect(url_for('index_view'))
        
    # Простая HTML-форма вместо шаблона
    return f"""
    <h1>Добавить мнение</h1>
    <a href="/">На главную</a>
    <form method="POST">
        {form.csrf_token}
        <p>Название: {form.title()}</p>
        <p>Текст: {form.text()}</p>
        <p>Ссылка: {form.source()}</p>
        <p>{form.submit()}</p>
    </form>
    """

@app.route('/story')
def random_story_view():
    opinions = Opinion.query.all()
    if not opinions:
        return "В базе пока нет рассказов."
    random_opinion = choice(opinions)
    return f"<h1>{random_opinion.title}</h1><p>{random_opinion.text}</p><a href='/'>На главную</a>"