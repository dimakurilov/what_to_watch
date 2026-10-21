import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from settings import Config

# Создаем приложение
app = Flask(__name__)
app.config.from_object(Config)

# Инициализируем базу данных
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# ВАЖНО: Импорты модулей строго в самом конце, чтобы избежать циклического импорта!
from . import views, models, forms, error_handlers, cli_commands