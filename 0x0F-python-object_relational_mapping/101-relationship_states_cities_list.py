#!/usr/bin/python3
""" Get a state
"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}\
'.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    all = session.query(State).all()
#     dictionary = {}
#     for state in all:
#         dictionary['{}: {}\
# '.format(state[0].id, state[0].name)] = []
#         for __ in all:
#             if state[0].name == __[0].name:
#                 dictionary['{}: {}\
# '.format(state[0].id, state[0].name)].append('\t{}: {}\
# '.format(__[1].id, __[1].name))
    for state in all:
        print('{}: {}\
'.format(state.id, state.name))
        for city in state.cities:
            print('\t{}: {}\
'.format(city.id, city.name))
