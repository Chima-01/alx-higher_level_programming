#!/usr/bin/python3
"""
    A script that prints the State object with the name
    passed as argument from the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states(user, passwd, database, state_name):
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(user, passwd, database),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = (
        session.query(State)
               .filter(State.name == state_name)
               .first()
            )

    if not state:
        print('Not found')
    else:
        print(f'{state.id}')

    session.close()


if __name__ == "__main__":
    if sys.argv[4]:
        list_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
