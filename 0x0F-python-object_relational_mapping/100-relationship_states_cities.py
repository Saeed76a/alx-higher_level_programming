#!/usr/bin/python3
""" Get a state
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}\
'.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    new_state = State(name='California')
    session.add(new_state)
    session.commit()
    new_city = City(name='San Francisco', state_id=new_state.id)
    session.add(new_city)
    session.commit()
