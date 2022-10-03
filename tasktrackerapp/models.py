from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String, nullable=False)
    desription = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)
    deadline = db.Column(db.Datetime, nullable=True)

    def __repr__(self):
        return f"Task {self.id} {self.name} in status {self.status}"
