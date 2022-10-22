import sys
from tasktrackerapp.models import Statuses, db
from tasktrackerapp import create_app

app = create_app()

with app.app_context():
    status_open = Statuses(
                name="OPEN",
                description="Статус используется когда задача только создана и не взята в работу"
                )
    status_in_work = Statuses(
                name="IN WORK",
                description="Статус используется когда задача взята в работу. но не выполнена"
                )
    status_in_review = Statuses(
                name="IN REVIEW",
                description="Статус используется когда задача выполнена и требует проверки"
                )
    status_done = Statuses(
                name="DONE",
                description="Статус используется когда задача выполнена и прошла проверку"
                )
    
    db.session.add(status_open)
    db.session.add(status_in_work)
    db.session.add(status_in_review)
    db.session.add(status_done)
    db.session.commit()
