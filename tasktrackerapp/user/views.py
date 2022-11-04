from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from flask import Blueprint, render_template, flash, redirect, url_for
from tasktrackerapp.user.forms import LoginForm
from tasktrackerapp.user.models import Users
from tasktrackerapp.task.models import Tasks

from tasktrackerapp.db import db

blueprint = Blueprint('user', __name__, url_prefix='/users')

@blueprint.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    title = "Авторизация"
    login_form = LoginForm()
    return render_template('login.html', page_title=title, form=login_form) 


@blueprint.route('/user.process-login', methods=['GET','POST'])
def process_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter(Users.login == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            flash('Вы успешли авторизировались')
            return redirect(url_for('index'))
    flash('Неправильное имя или пароль')
    return redirect(url_for('user.login'))


@blueprint.route('/logout')
def logout():
    logout_user()
    flash('Вы вышли из аккаунта')
    return redirect(url_for('index'))


@blueprint.route('/all_users')
@login_required
def all_users():
    title = "Все пользователи"
    users = Users.query.order_by(Users.id).all()
    return render_template('all_users.html', title=title, users=users)
    
@blueprint.route('/user/<int:id>')
@login_required
def user(id):
    sel_user = Users.query.get(id)
    user_tasks = Tasks.query.filter(Tasks.responsible == sel_user.firname_lasname)
    return render_template('user.html', user=sel_user, user_tasks=user_tasks)




@blueprint.route('/my_tasks')
@login_required
def my_tasks():
    title = "Мои задачи"
    user = current_user.firname_lasname
    tasks = Tasks.query.filter(Tasks.responsible == user).all()
    return render_template('my_tasks.html', title = title, tasks = tasks)

