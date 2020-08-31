#!/usr/bin/python3
""" prints the State object with the name passed as argument
from the database hbtn_0e_6_usa"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def print_func():
    if (len(argv) != 5):
        return

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    flag = 0
    for elem in session.query(State):
        if argv[4] == elem.name:
            print("{}".format(elem.id))
            flag = 1
    if flag == 0:
        print("Not found")

    session.close()


if __name__ == "__main__":
    print_func()
