from getpass import getpass
import sys
from tasktrackerapp.models import Users, db
from tasktrackerapp import create_app

app = create_app()

with app.app_context():
    username = input('Введите логин')
    username_fnln = input('Введите имя и фамилию')
    username_mail = input('Введите почту')
    if Users.query.filter(Users.login == username).count():
        print('Пользователь с таким именем уже существует')
        sys.exit(0)

    password1 = getpass("Введите пароль")
    password2 = getpass("Повторите пароль")
    
    if not  password1 == password2:
        print("Пароли не совпадают")
        sys.exit()

    new_user= Users(login = username, role='admin', firname_lasname=username_fnln, email='admin')
    new_user.set_password(password1)

    db.session.add(new_user)
    db.session.commit()

    print('Пользователь создан')