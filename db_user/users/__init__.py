from flask import Flask, render_template, flash, redirect, url_for
from users.models import db, User
from users.forms import LoginForm, AddForm, DeleteForm
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from users.db import db_session
from users.models import User, db
from werkzeug.security import generate_password_hash, check_password_hash


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route('/')
    def index():
        return render_template('index.html')


    @app.route('/login')
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        title = "Авторизация"
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form)


    @app.route('/process-login', methods=['GET','POST'])
    def process_login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter(User.login == form.username.data).first()
            if user and user.check_password(form.password.data):
                login_user(user)
                flash('Вы успешли авторизировались')
                return redirect(url_for('index'))

        flash('Неправильное имя или пароль')
        return redirect(url_for('login'))


    @app.route('/logout')
    def logout():
        logout_user()
        flash('Вы вышли из аккаунта')
        return redirect(url_for('index'))

    
    @app.route('/admin')
    @login_required
    def admin():
        form = AddForm()
        form2 = DeleteForm()
        if current_user.role == 'admin':
            return render_template('admin.html', title = 'Sign In', form = form, form2 = form2)
        else:
            return redirect(url_for('index'))
        

    @app.route('/add_user', methods = ['POST', 'GET'])
    def add_user():
        form = AddForm()
        if form.validate_on_submit():

            login = form.login.data
            password1 = form.password.data
            password2 = form.password.data
            firname_lasname = form.firname_lasname.data
            email = form.email.data
            role = form.role.data
            user_info = User(login=login, firname_lasname=firname_lasname, email=email, role=role)
            user_info.set_password(password1)
            db_session.add(user_info)
            db_session.commit()
            
        flash('Пользователь добавлен')
        return redirect(url_for('admin'))



    @app.route('/del_user', methods = ['POST', 'GET'])
    def del_user():
        form = DeleteForm()
        if form.validate_on_submit():
            inp_login = form.del_login.data
            search = db_session.query(User).filter(User.login == inp_login).one()
            db_session.delete(search)
            db_session.commit()
        flash('Пользователь удален')
        return redirect(url_for('admin'))



    return app 