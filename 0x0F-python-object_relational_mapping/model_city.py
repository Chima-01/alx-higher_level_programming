#!/usr/bin/python3
"""
    import module for sqlalchemy
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

db = 'mysql+mysqldb://root:root@localhost:3306/hbtn_0e_6_usa'
engine = create_engine(db)

Base = declarative_base()


class City(Base):
    """ class to inherit from declarative_base """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer,  ForeignKey("states.id"), nullable=False)
