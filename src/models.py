import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nick_name = Column(String(50), unique=True, nullable=False)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String, unique=True, nullable=False)
    password = Column(String, unique=False, nullable=False)

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    photo = Column(String, nullable=False)
    text = Column(String(350))
    user_id = Column(Integer, ForeignKey('user.id')) #estas 2 últimas líneas son obligatorias para hacer las relaciones
    user = relationship('User')

class comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    message = Column(String(300))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User')
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship('Post')

class direct_message(Base):
    __tablename__ = 'direct_message'
    id = Column(Integer, primary_key=True)
    sender_id = Column(String, ForeignKey('user.id'))
    recibed_id = Column(String, ForeignKey('user.id'))
    message = Column(String(300))
    user = relationship('User')


    def to_dict(self):
        return {}


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')