import csv
from . import app, db
from .models import Opinion
@app.cli.command('load_opinions')
def load_opinions_command():
    """Загружает мнения из файла opinions.csv в базу данных."""
    with open('opinions.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        count = 0
        for row in reader:
            if not Opinion.query.filter_by(text=row['text']).first():
                opinion = Opinion(
                    title=row['title'],
                    text=row['text'],
                    source=row['source']
                )
                db.session.add(opinion)
                count += 1
        db.session.commit()
    print(f'Успешно загружено {count} новых мнений!')