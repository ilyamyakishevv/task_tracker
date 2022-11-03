task_tracker_project
======================

Веб-приложение, корпоративный трэкер-задач предназначенное для создания повседневных, рабочих задач на отдельных пользоваетелей и мониторинга выполнения и текущего статуса задач. 


Функционал приложения
---------------------
- Логин
- Добавление / удаление пользователей с разными ролями
- Добавление / удаление и изменение задач
- Отображение информации о текущих задачах для всех пользователей / для каждого отдельного пользоваетля
- Отображение уведомлений о действиях с задачами (смена статусов, удаление, изменение, добавление)

Установка
==========
Создайте виртуальное окружение и активируйте его. Установите зависимости:

    pip install -r requirements.txt


Настройка
---------
- Cконфигурируйте приложение, для этого запустите скрипт (при необходиости отредактируйте конфиг используя собственные значения)

   `$ python create_config.py `
 
- Примените миграции к своей БД, для этого нужно выполнить в консоли следующие операции:

Установить переменную среды

    $ export FLASK_APP=tasktrackerapp


Применить изменения к БД

    $ flask db upgrade


- Заполните БД статусами, ролями пользователей и возможными действиями с задачами (при необходимости можете добавить свои роли, статусы или действия, отредоактировав скрипт):


`$ python create_statuses_roles_changes.py`


- Создайте перввого админн-пользователя запустив скрипт: 

     `$ python create_admin.py`

Запуск
=======
В консоли (не забудьте активировать виртуальное окружение) пропишите:


    $ run.sh  (для Linux)
    

    >run.bat  (для Windows)


