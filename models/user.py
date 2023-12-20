#!/usr/bin/python3
<<<<<<< HEAD
"""This module defines a class User"""
=======
"""User class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review
>>>>>>> 30de344cde7ddeaa6171b787a1808505ab1441bc

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review

<<<<<<< HEAD
Base = declarative_base()

class User(BaseModel, Base):
    """This class defines a user by various
    attributes
       email = ''
       password = ''
       first_name = ''
       last_name = ''
    """

    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
=======
class User(BaseModel, Base):
    """This is class for user """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
>>>>>>> 30de344cde7ddeaa6171b787a1808505ab1441bc
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="user")
    reviews = relationship("Review", cascade='all, delete, delete-orphan',
                           backref="user")
