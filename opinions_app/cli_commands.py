import csv
from . import app, db
from .models import Opinion
@app.cli.command('load_opinions')
def load_opinions_command():
    """Загружает мнения из файла opinions.csv в базу данных."""
    # Вставьте сюда ваш код из старого файла opinions_app.py
    # Пример:
    with open('opinions.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            opinion = Opinion(
                title=row['title'],
                text=row['text'],
                source=row['source']
            )
            db.session.add(opinion)
        db.session.commit()
    print('Данные загружены!')