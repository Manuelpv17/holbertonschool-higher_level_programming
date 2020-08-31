#!/usr/bin/python3
""" lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa"""

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

    for st in session.query(State).order_by(State.id):
        print("{}: {}".format(st.id, st.name))
        for ci in st.cities:
            print("\t{}: {}".format(ci.id, ci.name))

    session.close()


if __name__ == "__main__":
    print_func()
