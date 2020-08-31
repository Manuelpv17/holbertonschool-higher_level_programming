#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys


def list_func():
    """ lists all states from the database hbtn_0e_0_usa """
    if len(sys.argv) != 4:
        return

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states;")

    r = cursor.fetchall()
    for elem in r:
        print(elem)

    db.close()


if __name__ == "__main__":
    list_func()
