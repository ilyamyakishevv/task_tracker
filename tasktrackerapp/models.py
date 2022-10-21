from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_manager

db = SQLAlchemy()


class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String, index=True, nullable=False)
    description = db.Column(db.String, nullable=False)
    creator = db.Column(db.String, nullable=False)
    responsible = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False, default="OPEN")
    deadline = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f"Task {self.id} {self.name} in status {self.status}"


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(), index=True, unique = True)
    password = db.Column(db.String(128))
    firname_lasname = db.Column(db.String(), index=True)
    email = db.Column(db.String)
    role = db.Column(db.Text, nullable=True)
    phone = db.Column(db.Integer)


    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def is_admin(self):
        return self.role == 'admin' 

    def __repr__(self):
        return 'Сотрудник - {}'.format(self.firname_lasname)
    
    # class Statuses(db.Model):
    #     id = db.Column(db.Integer, primary_key=True, unique=True)
    #     name = db.Column(db.String, index=True, nullable=False)
    #     description = db.Column(db.String, index=True, nullable=True)