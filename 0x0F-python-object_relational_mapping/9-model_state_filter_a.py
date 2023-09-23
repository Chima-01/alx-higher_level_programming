#!/usr/bin/python3
"""
import state and model from model_state module

A script that lists all State objects that contain
the letter a from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv

if __name__ == '__main__':
    db = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}'
    engine = create_engine(db)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.like('%a')).\
        order_by(State.id).all()

    for state in states:
        print(f'{state.id}: {state.name}')

    session.commit()
    session.close()
