from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    department = db.Column(db.String())
    email = db.Column(db.String(120), unique=True)

    def __repr__(self):
        return f'Сотрудник - {self.name}, {self.department}, {self.email}'

