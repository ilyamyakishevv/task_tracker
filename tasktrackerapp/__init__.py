from flask import Flask, render_template
from tasktrackerapp.models import db


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app_title = "Task tracker LP26 project"
    message = "Project is still in progress"

    @app.route('/')
    def index():
        return render_template('index.html', title=app_title, message=message)
    return app
