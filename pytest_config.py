import pytest

from tasktrackerapp import create_app
from tasktrackerapp.user.models import Users
from tasktrackerapp import db
from tasktrackerapp import config
from tasktrackerapp.task.models import Tasks


class TestConfig(config): 
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    WTF_CSRF_ENABLED = False
    HOST = '127.0.0.1'
    PORT = '5555'
    SERVER_NAME = '127.0.0.1:5555'
