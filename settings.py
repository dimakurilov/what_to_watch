import os

from dotenv import load_dotenv


# Загрузка переменных окружения
load_dotenv()


# Настройки приложения
class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'SQLALCHEMY_DATABASE_URI', 'sqlite:///db.sqlite3'
    )
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
