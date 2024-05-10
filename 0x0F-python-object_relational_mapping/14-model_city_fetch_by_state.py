#!/usr/bin/python3
"""
    A script that lists all City objects from the database
    hbtn_0e_14_usa
"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def list_cities(user, passwd, database):
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (user, passwd, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state, city in session.query(State, City).\
            filter(State.id == City.state_id).\
            all():
        print(f'{state.name}: ({city.id}) {city.name}')
    session.close()


if __name__ == '__main__':
    if sys.argv[3]:
        list_cities(sys.argv[1], sys.argv[2], sys.argv[3])
