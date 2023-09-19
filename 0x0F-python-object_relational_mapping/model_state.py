#!/usr/bin/python3
"""
    import module for sqlalchemy
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

db = 'mysql+mysqldb://root:root@localhost:3306/hbtn_0e_6_usa'
engine = create_engine(db)

Base = declarative_base()


class State(Base):
    """ class to inherit from declarative_base """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
