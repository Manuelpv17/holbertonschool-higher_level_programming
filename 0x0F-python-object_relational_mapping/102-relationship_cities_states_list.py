#!/usr/bin/python3
""" lists all City objects from the database"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


def print_func():
    if (len(argv) != 4):
        return

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for ci in session.query(City).order_by(City.id):
        print("{}: {} -> {}".format(ci.id, ci.name, ci.state.name))

    session.close()


if __name__ == "__main__":
    print_func()
