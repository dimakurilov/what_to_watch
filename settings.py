import os
from dotenv import load_dotenv

# Загружаем переменные из .env файла вручную
load_dotenv()

class Config(object):
    # Если переменная в .env не найдена, используем значение по умолчанию
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///db.sqlite3')
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')