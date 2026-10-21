from . import app

# noqa: E302
@app.errorhandler(404)
def page_not_found(error):
    return "Страница не найдена (404)", 404

# noqa: E302
@app.errorhandler(500)
def internal_error(error):
    return "Внутренняя ошибка сервера (500)", 500
# конец файла (обязательно нажмите Enter здесь)