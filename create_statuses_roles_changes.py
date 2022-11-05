from tasktrackerapp.db import Changes, Statuses, Roles, db
from tasktrackerapp import create_app


def create_statuses():
    status_dict = {
            "OPEN" : "Статус используется когда задача только создана и не взята в работу",
            "IN WORK" : "Статус используется когда задача взята в работу. но не выполнена",
            "IN REVIEW" : "Статус используется когда задача выполнена и требует проверки",
            "DONE" : "Статус используется когда задача выполнена и прошла проверку"
        }
    for name in status_dict: 
        db.session.add(Statuses(name=name, description=status_dict[name]))
        db.session.commit() 
        
def create_roles():
    roles_list = ["admin", "user"]
    for name in roles_list:
        db.session.add(Roles(role=name))
        db.session.commit() 


def create_changes():
    changes_list = [
            ("ADD TASK","добавил задачу"),
            ("DELETE TASK", "удалил задачу"),
            ("EDIT TASK", "изменил задачу"),
            ("STATUS IN WORK","взял в работу задачу"),
            ("STATUS IN REVIEW", "выполнил задачу"),
            ("STATUS DONE","одобрил задачу"),
            ("STATUS IN WORK AGAIN", "отправил на доработку задачу"),
            ("CANCELATION", "отменил выполнение задачи"), 
            ("COMMENT", "оставил комментарий к задаче")
    ]
    for change in changes_list: 
        name, desc = change
        db.session.add(Changes(name=name, description=desc))
        db.session.commit() 

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        create_statuses()
        create_roles()
        create_changes()