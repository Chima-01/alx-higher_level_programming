#!/usr/bin/python3
"""
import state and model from model_state module

a script print all cities
in database hbtn_0e_14_usa
"""
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv

if __name__ == '__main__':
    if argv[3]:
        db = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}'
        engine = create_engine(db, pool_pre_ping=True)

        Session = sessionmaker(bind=engine)
        session = Session()
        cities = session.query(City, State).filter(City.state_id == State.id)\
            .order_by(City.id).all()

        if cities:
            for city, state in cities:
                print(f'{state.name}: ({city.id}) {city.name}')

        session.commit()
        session.close()
