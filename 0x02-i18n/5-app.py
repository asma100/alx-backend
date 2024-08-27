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

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user(user_id):
    """Retrieves user information by ID if it exists."""
    try:
        return users[int(user_id)]
    except (KeyError, ValueError):
        return None


@app.before_request
def before_request():
    """
    Sets the current user based on the 'login_as' parameter.
    """
    user_id = request.args.get('login_as')
    g.user = get_user(user_id) if user_id else None

@babel.localeselector
def get_locale():
    """locale"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def Welcome():
    """welcome"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
