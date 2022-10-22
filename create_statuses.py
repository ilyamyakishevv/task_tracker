from tasktrackerapp.models import Statuses, db
from tasktrackerapp import create_app


def create_statuses():
    app = create_app()
    with app.app_context():
        status_dict = {
                    "OPEN" : "Статус используется когда задача только создана и не взята в работу",
                    "IN WORK" : "Статус используется когда задача взята в работу. но не выполнена",
                    "IN REVIEW" : "Статус используется когда задача выполнена и требует проверки",
                    "DONE" : "Статус используется когда задача выполнена и прошла проверку"
        }
        
        for name in status_dict: 
            db.session.add(Statuses(name=name, description=status_dict[name]))
        db.session.commit()

if __name__ == '__main__': 
    create_statuses()