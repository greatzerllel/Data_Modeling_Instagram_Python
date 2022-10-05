import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(80), nullable=False)
    password = Column(String(50), nullable=False)

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    hair_color = Column(String(250))
    homeworld = Column(String(250))
    eye_color = Column(String(250))
    gender = Column(String(250)) 

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    diameter = Column(String(50))
    rotation_period = Column(String(50))
    orbital_period = Column(String(50))
    gravity = Column(String(50))
    population = Column(String(50))
    climate = Column(String(50))

class Planet_terrain(Base):
    __tablename__ = 'planets_terrains'
    planet_id = Column(Integer, ForeignKey('planets.id'), primary_key=True)
    terrain = Column(Integer, ForeignKey('terrains.id'),  primary_key=True)

class Terrain(Base):
    __tablename__ = 'terrains'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

class Favorite(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)
    character = relationship(Character)
    planet = relationship(Planet)

class Favorites_group(Base):
    __tablename__ = 'favorites_group'
    favorite_character_id = Column(Integer, ForeignKey('favorite_character.id'), primary_key=True)
    favorite_planet_id = Column(Integer, ForeignKey('favorite_planet.id'),  primary_key=True)

class Favorite_character(Base):
    __tablename__ = 'favorite_character'
    id = Column(Integer, primary_key=True)
    Favorites= Column(Integer, ForeignKey('favorites.id'))
    Character_id = Column(Integer, ForeignKey('characters.id'))

class Favorite_planet(Base):
    __tablename__ = 'favorite_planet'
    id = Column(Integer, primary_key=True)
    Favorites = Column(Integer, ForeignKey('favorites.id'))
    Planets_id = Column(Integer, ForeignKey('planets.id'))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')