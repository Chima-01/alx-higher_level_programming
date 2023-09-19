#!/usr/bin/python3
"""
import state and model from model_state module

A script that prints the State object with the name passed
as argument from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv

if __name__ == '__main__':
    if argv[4]:
        db = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}'
        engine = create_engine(db, pool_pre_ping=True)

        Session = sessionmaker(bind=engine)
        session = Session()
        status = argv[4]
        state = session.query(State).filter(State.name == status).first()

        if state:
            print(f'{state.id}')
        else:
            print('Not found')

    session.commit()
    session.close()
