#!/usr/bin/python3
"""
import state and model from model_state module

a script that update the State name
in the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv

if __name__ == '__main__':
    if argv[3]:
        db = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}'
        engine = create_engine(db, pool_pre_ping=True)

        Session = sessionmaker(bind=engine)
        session = Session()
        state = session.query(State).filter_by(id=2).first()

        if state:
            state.name = "New Mexico"

        session.commit()
        session.close()