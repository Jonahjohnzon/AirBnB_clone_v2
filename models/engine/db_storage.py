#!/usr/bin/python3
"""SQLAlchemy"""
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """MySQL Database storage engine SQLAlchemy"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize a new instance of the DBStorage class.

        The __init__ method creates a new instance of the DBStorage class
        and configures the SQLAlchemy engine for MySQL database connection.
        database, and host. If the environment is set to "test", existing tables
        are dropped for a clean testing environment.

        Args:
            None

        Returns:
            None
        """
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """return a dictionary"""
        my_dict = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                my_dict[key] = elem
        else:
            classes = [State, City, User, Place, Review, Amenity]
            for c in classes:
                query = self.__session.query(c)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    my_dict[key] = elem
        return my_dict

    def new(self, obj):
        """add new element in table"""
        self.__session.add(obj)

    def save(self):
        """save changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete an element in table"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """configuration"""
        Base.metadata.create_all(self.__engine)
        sect = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sect)
        self.__session = Session()

    def close(self):
        """call remove()"""
        self.__session.close()

