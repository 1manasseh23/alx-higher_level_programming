#!/usr/bin/python3
"""
This a Python file similar to model_state.py named model_city.py
that contains the class definition of a City.

City class:
inherits from Base (imported from model_state)
links to the MySQL table cities
class attribute id that represents a column of an auto-generated,
unique integer, can’t be null and is a primary key
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base

Base = declarative_base()


class City(Base):
    __tablename__ = 'cities'
    id = Column(
            Integer, primary_key=True, nullable=False, autoincrement=True
            )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
