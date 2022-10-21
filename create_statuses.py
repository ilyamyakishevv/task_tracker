import sys
from tasktrackerapp.models import Statuses, db
from tasktrackerapp import create_app

app = create_app()

with app.app_context():
    status_name = input('Введите название статуса: ')
    if Statuses.query.filter(Statuses.name == status_name).count():
        print('Такой статус уже существует! Название статуса должно быть уникальным!')
        sys.exit(0)
    status_descriprion = input("Введите описание статуса (по желанию): ")

    new_status = Statuses(name = status_name, description=status_descriprion)

    db.session.add(new_status)
    db.session.commit()
