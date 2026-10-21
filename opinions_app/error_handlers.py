from flask import render_template
from . import app

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# Если у вас были другие обработчики (500 и т.д.), добавьте их сюда