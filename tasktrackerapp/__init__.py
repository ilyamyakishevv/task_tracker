from flask import Flask, render_template
from tasktrackerapp.models import db
from tasktrackerapp.task_add_form import TaskAdd


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app_title = "Task tracker LP26 project"
    message = "Project is still in progress"

    @app.route('/')
    def index():
        return render_template('index.html', title=app_title, message=message)
       
    @app.route('/add_task')
    def add_task():
        title = "Добавить задачу"
        add_task_form = TaskAdd()
        return render_template('add_task.html', title=title, form=add_task_form)
    return app 
