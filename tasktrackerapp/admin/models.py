from tasktrackerapp.db import db


class Roles(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    role = db.Column(db.String, unique=True)
