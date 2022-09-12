#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, Session
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

USER = getenv('HBNB_MYSQL_USER')
PASS = getenv('HBNB_MYSQL_PWD')
HOST = getenv('HBNB_MYSQL_HOST')
DB = getenv('HBNB_MYSQL_DB')

class DBStorage:
    """Class DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiates a new database"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(USER, PASS, HOST, DB), pool_pre_ping=True)

        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Return a dictionary all cls in DB o all obj un DB"""
        dict_return = {}
        if cls:
            for obj in self.__session.query(cls).all():
                dict_return[obj.to_dict()['__class__'] + '.' + obj.id] = obj
        else:
            list_class = [State, Place, User, City, Review, Amenity]
            for every_class in list_class:
                for obj in self.__session.query(every_class).all():
                    dict_return[obj.to_dict()['__class__'] + '.' + obj.id] = obj
        return dict_return

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()
