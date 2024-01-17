# models/engine/db_storage.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
import os

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user = os.environ.get('HBNB_MYSQL_USER')
        pwd = os.environ.get('HBNB_MYSQL_PWD')
        host = os.environ.get('HBNB_MYSQL_HOST', default='localhost')
        db = os.environ.get('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, pwd, host, db),
                                      pool_pre_ping=True)
        if os.environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        # TODO: Implement the all method
        pass

    def new(self, obj):
        # TODO: Implement the new method
        pass

    def save(self):
        # TODO: Implement the save method
        pass

    def delete(self, obj=None):
        # TODO: Implement the delete method
        pass

    def reload(self):
        # TODO: Implement the reload method
        pass
