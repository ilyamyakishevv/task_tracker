from crypt import methods
from xxlimited import new
from flask import Flask, render_template, flash, redirect, url_for
from tasktrackerapp.models import Tasks, db
from tasktrackerapp.task_add_form import TaskAdd


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app_title = "Task tracker LP26 project"
    message = "Project is still in progress"
    db.init_app(app)

    @app.route('/')
    def index():
        return render_template('index.html', title=app_title, message=message)
       
    @app.route('/add_task')
    def add_task():
        title = "Добавить задачу"
        add_task_form = TaskAdd()
        return render_template('add_task.html', title=title, form=add_task_form)

    @app.route('/adding_task', methods=['POST'])
    def adding_task():
        adding_form = TaskAdd() 
        if adding_form.validate_on_submit(): 
            task_name = adding_form.name.data
            task_description = adding_form.description.data
            task_deadline = adding_form.deadline.data
            new_task = Tasks(name=task_name, desription = task_description, status='OPEN', deadline = task_deadline)
            db.session.add(new_task)
            db.session.commit()
            flash ("Задание успешно добавлено")
            return redirect(url_for('add_task'))
        flash ("Заполните все поля!")
        return redirect(url_for('add_task'))


           
    return app 
