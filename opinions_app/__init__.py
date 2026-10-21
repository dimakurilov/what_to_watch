from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Обратите внимание на две точки! Это значит "подняться на уровень выше" в папку what_to_watch
from ..settings import Config 

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Импорты строго в конце!
from . import views, models, forms, error_handlers, cli_commands