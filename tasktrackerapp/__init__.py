from flask import Flask, render_template
from tasktrackerapp.db import db
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate
from tasktrackerapp.user.views import blueprint as user_blueprint
from tasktrackerapp.task.views import blueprint as task_blueprint
from tasktrackerapp.admin.views import blueprint as admin_blueprint
from tasktrackerapp.user.models import Users
from tasktrackerapp.task.models import Actions

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    app.register_blueprint(user_blueprint)
    app.register_blueprint(task_blueprint)
    app.register_blueprint(admin_blueprint)
    
    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(user_id)


    @app.route('/')
    @login_required
    def index():
        actions = Actions.query.order_by(Actions.action_date).all()
        main_page_users = Users.query.all()
        return render_template('index.html', users=main_page_users, actions=actions) 
    return app