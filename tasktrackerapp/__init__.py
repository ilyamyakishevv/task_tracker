from flask import Flask, render_template, flash, redirect, url_for
from tasktrackerapp.models import Tasks, Users, db
from tasktrackerapp.task_add_form import TaskAdd
from tasktrackerapp.forms import LoginForm, AddForm, DeleteForm
from datetime import date
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from tasktrackerapp.database import db_session
from werkzeug.security import generate_password_hash, check_password_hash



def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app_title = "Task tracker LP26 project"
    message = "Project is still in progress"
    db.init_app(app)
   
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(user_id)

    @app.route('/')
    def index():
        return render_template('index.html', title=app_title, message=message)

    @app.route('/add_task')
    def add_task():
        title = "Добавить задачу"
        add_task_form = TaskAdd()
        return render_template(
                        'add_task.html',
                        title=title,
                        form=add_task_form
                        )

    @app.route('/adding_task', methods=['POST'])
    def adding_task():
        adding_form = TaskAdd()
        if adding_form.validate_on_submit():
            task_name = adding_form.name.data
            task_description = adding_form.description.data
            task_deadline = adding_form.deadline.data
            if task_deadline < date.today():
                flash("Ввелите корректную дату!")
                return redirect(url_for('add_task'))
            new_task = Tasks(
                name=task_name,
                description=task_description,
                status='OPEN',
                deadline=task_deadline
                )
            db.session.add(new_task)
            db.session.commit()
            flash("Задание успешно добавлено")
            return redirect(url_for('add_task'))
        flash("Заполните все поля!")
        return redirect(url_for('add_task'))



    @app.route('/login')
    def login():
        """ if current_user.is_authenticated: """
        """     return redirect(url_for('index')) """
        title = "Авторизация"
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form) 


    @app.route('/process-login', methods=['GET','POST'])
    def process_login():
        form = LoginForm()
        if form.validate_on_submit():
            user = Users.query.filter(Users.login == form.username.data).first()
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
            user_info = Users(login=login, firname_lasname=firname_lasname, email=email, role=role)     
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
            search = db_session.query(Users).filter(Users.login == inp_login).one()
            db_session.delete(search)
            db_session.commit()
        flash('Пользователь удален')
        return redirect(url_for('admin'))
        
    return app