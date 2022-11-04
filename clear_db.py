from tasktrackerapp.models import Changes, Statuses, Roles, Actions, Tasks, db
from tasktrackerapp import create_app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.session.query(Actions).delete()
        db.session.query(Changes).delete()
        db.session.query(Statuses).delete()
        db.session.query(Roles).delete()
        db.session.query(Tasks).delete()
        db.session.commit()