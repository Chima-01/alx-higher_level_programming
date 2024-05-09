#!/usr/bin/python3
"""
    A script that prints the State object with the name
    passed as argument from the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states(user, passwd, database):
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(user, passwd, database),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    new_state = session.query(State).filter(State.name == 'Louisiana').first()
    print(f'{new_state.id}')

    session.close()


if __name__ == "__main__":
    if sys.argv[3]:
        list_states(sys.argv[1], sys.argv[2], sys.argv[3])
