from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_manager
from sqlalchemy.orm import relationship

from tasktrackerapp.db import db


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(), index=True, unique=True)
    password = db.Column(db.String(128))
    firname_lasname = db.Column(db.String(), index=True)
    email = db.Column(db.String)
    role = db.Column(db.String, nullable=True)
    action = relationship('Actions', backref='users')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def is_admin(self):
        return self.role == 'admin'

    def __repr__(self):
        return 'Сотрудник - {}'.format(self.firname_lasname)
