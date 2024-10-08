#!/usr/bin/python3
"""
     A python file that contains the class definition of a State
     and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_city import City

Base = declarative_base()


class State(Base):
    """ class to create a table """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    state = relationship(City, back_populates="state",
            cascade="all, delete, delete-orphan")
