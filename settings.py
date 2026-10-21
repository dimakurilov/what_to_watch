import os

from dotenv import load_dotenv

# noqa: E302
load_dotenv()

# noqa: E302
class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'SQLALCHEMY_DATABASE_URI', 'sqlite:///db.sqlite3'
    )
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
# конец файла (обязательно нажмите Enter здесь)