#!/usr/bin/python3
""" Get a state
"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}\
'.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    state_obj = State()
    state_obj.name = 'California'
    city_obj = City()
    city_obj.name = 'San Francisco'
    state_obj.cities.append(city_obj)
    session.add_all([state_obj, city_obj])
    session.commit()
    session.close()
