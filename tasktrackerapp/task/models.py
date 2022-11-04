from sqlalchemy.orm import relationship
from tasktrackerapp.db import db
from datetime import datetime


class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String, index=True, nullable=False)
    description = db.Column(db.String, nullable=False)
    creator = db.Column(db.String, nullable=False)
    responsible = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False, default="OPEN")
    deadline = db.Column(db.DateTime, nullable=True)
    is_deleted = db.Column(db.Boolean, nullable=False)
    action = relationship('Actions', backref='tasks')

    def comments_count(self):
        return Comment.query.filter(Comment.task_id == self.id).count()

    def __repr__(self):
        return f"Task {self.id} {self.name} in status {self.status}"


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text(), nullable = False)
    created = db.Column(db.DateTime, nullable = False, default = datetime.now())
    task_id = db.Column(
        db.Integer,
        db.ForeignKey('tasks.id', ondelete = 'CASCADE'),
        index=True
    )
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', ondelete='CASCADE'),
        index=True
    )
    tasks = relationship('Tasks', backref='comments')
    user = relationship('Users', backref='comments')

    def __repr__(self):
        return '<Comment {}>'.format(self.id)


class Changes(db.Model): 
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String, index=True, unique=True, nullable=False)
    description = db.Column(db.String, index=True, nullable=True)
    action = relationship('Actions', backref='changes')
    


class Actions(db.Model): 
    id = db.Column(db.Integer, primary_key=True, unique=True)
    action_user = db.Column(db.Integer, db.ForeignKey(
        'users.id', 
        ondelete='CASCADE'),
        index=True
        )
    action_object = db.Column(db.Integer, db.ForeignKey(
        'tasks.id', 
        ondelete='CASCADE'),
        index=True
        )
    action_description = db.Column(db.Integer, db.ForeignKey(
        'changes.id',
        ondelete='CASCADE'),
        index=True
        )
    action_date = db.Column(db.DateTime, nullable=True, default=datetime.now())
    ADD_TASK = 1 
    DELETE_TASK = 2
    EDIT_TASK = 3
    STATUS_IN_WORK = 4
    STATUS_IN_REVIEW = 5
    STATUS_DONE = 6
    STATUS_IN_WORK_AGAIN = 7
    CANCELATION = 8
    COMMENT = 9
