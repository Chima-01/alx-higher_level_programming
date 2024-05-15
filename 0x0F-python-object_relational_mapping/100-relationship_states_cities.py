#!/usr/bin/python3
"""
    A script that add state to database
"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State


def add_states(user, passwd, database):
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (user, passwd, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State("California")
    new_state.state = "San Francisco"
    session.add(new_state)
    session.commit()
    session.close()


if __name__ == '__main__':
    if sys.argv[3]:
        add_states(sys.argv[1], sys.argv[2], sys.argv[3])
