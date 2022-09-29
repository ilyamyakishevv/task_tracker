from db import db_session
from models import User
print('Добавить, Удалить, Изменить или Получить пользователя.')
a = 1
while a>0:
    what_todo=input(f'\n Что вы хотите сделать?\n Чтобы выйти из программы введите - exit\n')
    what_todo=what_todo.lower().replace(' ', '')

    if what_todo == 'добавить':
        user_info = User(name=input(f"Введите имя и фамилию:\n"), department=input(f"Из какого отдела сотрудник?\n"), email=input(f"Введите E-mail:\n"))
        db_session.add(user_info)
        db_session.commit()
        print('Пользователь добавлен!')

    elif what_todo == 'удалить':
        input_id = int(input("Введите id удаляемого объекта: "))
        search = db_session.query(User).filter(User.id == input_id).one()
        db_session.delete(search)
        db_session.commit()
        print("Пользователь удален!")
    
    elif what_todo == 'изменить':
        b = 1
        while b>0:
            input_id = int(input("Введите id изменяемого объекта: "))
            what_edit = input(f"Что вы хотите изменить?: name, email, department:\n")
            new_edit = input(f'Введите новое значение {what_edit}:\n')
            search = db_session.query(User).filter(User.id == input_id).update({what_edit: new_edit})
            db_session.commit()
            print(f'\nДанные пользователя изменены!')
            stop_cycle=input(f'Хотите изменить что-то еще? да/нет\n').lower().replace(' ','')
            if stop_cycle == 'да':
                b+=0
            elif stop_cycle == 'нет':
                b-=1

    elif what_todo == 'получить':
        input_id = int(input('Введите ID пользователя'))
        search = db_session.query(User).filter(User.id == input_id).one()
        print(search)

    elif what_todo == 'exit':
        a-=1
    
    else:
        print(f'\nКоманды не существует, введите команду из списка предложенных: Добавить, Удалить, Изменить, Получить')
    
