from flask import Flask, render_template, flash, redirect, url_for
from tasktrackerapp.models import Statuses, Tasks, Users, db
from tasktrackerapp.task_add_form import TaskAdd
from tasktrackerapp.forms import LoginForm, AddForm, DeleteForm
from datetime import date
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate



def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app_title = "Task tracker LP26 project"
    message = "Project is still in progress"
    db.init_app(app)
    migrate = Migrate(app, db)

   
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(user_id)


    @app.route('/')
    def index():
        main_page_users = Users.query.all()
        return render_template('index.html', title=app_title, message=message, users=main_page_users)

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
            task_creator = current_user.firname_lasname
            task_responsible = current_user.firname_lasname
            new_task = Tasks(
                name=task_name,
                description=task_description,
                status='OPEN',
                deadline=task_deadline,
                creator=task_creator,
                responsible=task_responsible
                )
            db.session.add(new_task)
            db.session.commit()
            flash("Задание успешно добавлено")
            return redirect(url_for('add_task'))
        flash("Заполните все поля!")
        return redirect(url_for('add_task'))

    @app.route('/all_users')
    def all_users():
        title = "Все пользователи"
        users = Users.query.order_by(Users.id).all()
        return render_template('all_users.html', title = title, users=users)
        
    @app.route('/user/<int:id>')
    def user(id):
        sel_user = Users.query.get(id)
        user_tasks = Tasks.query.filter(Tasks.responsible == sel_user.firname_lasname)
        return render_template('user.html', user=sel_user, user_tasks=user_tasks)


    @app.route('/view_tasks')
    def view_tasks():
        title = "Все задачи"
        tasks = Tasks.query.order_by(Tasks.id).all()
        return render_template('view_tasks.html', title=title, tasks=tasks) 

    @app.route('/task/<int:id>')
    def get_task(id):
        task = Tasks.query.get(id)
        return render_template('task.html', task=task) 
      
    @app.route('/task/<int:id>/delete')
    def delete_task(id):
        task = Tasks.query.get_or_404(id)
        try: 
            db.session.delete(task)
            db.session.commit()
            return redirect(url_for('view_tasks'))
        except:
            db.session.rollback()
            return flash("При удалении задания произошла ошибка")

    @app.route('/task/<int:id>/edit', methods=['POST', 'GET'])
    def edit_task(id):
        task = Tasks.query.get(id)
        edit_form = TaskAdd()
        statuses = Statuses.query.order_by(Statuses.id).all()
        if edit_form.validate_on_submit():
            task.name = edit_form.name.data
            task.description = edit_form.description.data
            task.deadline = edit_form.deadline.data
            if task.deadline < date.today():
                flash("Ввелите корректную дату!")
                return redirect(url_for('task_edit'))
            db.session.commit()
            flash("Задание успешно измненено")
            return redirect(url_for('view_tasks'))
        return render_template('edit_task.html', form=edit_form, statuses=statuses)


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
            db.session.add(user_info)  
            db.session.commit()         
            
        flash('Пользователь добавлен')
        return redirect(url_for('admin'))


    @app.route('/del_user', methods = ['POST', 'GET'])
    def del_user():
        form = DeleteForm()
        if form.validate_on_submit():
            inp_login = form.del_login.data
            search = db.session.query(Users).filter(Users.login == inp_login).one()
            db.session.delete(search)
            db.session.commit()
        flash('Пользователь удален')
        return redirect(url_for('admin'))
        
    return app