#!/usr/bin/python3
"""
import state and model from model_state module

a script that deletes State
in database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv

if __name__ == '__main__':
    if len(argv) == 4:
        db = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}'
        engine = create_engine(db, pool_pre_ping=True)

        Session = sessionmaker(bind=engine)
        session = Session()
        state_delete = session.query(State).filter(State.name.like('%a%'))\
            .all()

        for state in state_delete:
            session.delete(state)

        session.commit()
        session.close()
    else:
        pass
