#!/usr/bin/python3
"""
    A script that lists all State objects from the database
    hbtn_0e_6_usa
"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states(user, passwd, database):
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (user, passwd, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    all_states = session.query(State).all()
    for state in all_states:
        print(f'{state.id}: {state.name}')

    session.close()


if __name__ == '__main__':
    if sys.argv[3]:
        list_states(sys.argv[1], sys.argv[2], sys.argv[3])
