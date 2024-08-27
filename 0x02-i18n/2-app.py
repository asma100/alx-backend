#!/usr/bin/env python3
"""task 2"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """locale"""
    user_language =
    request.accept_languages.best_match(babel.supported_locales)
    return user_language


@app.route('/')
def Welcome():
    """welcome"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
