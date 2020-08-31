#!/usr/bin/python3
""" makes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument. """

import MySQLdb
import sys


def filter_func():
    """ func """
    if len(sys.argv) != 5:
        return

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states  ORDER BY states.id ASC;")

    r = cursor.fetchall()
    for elem in r:
        if sys.argv[4] == elem[1]:
            print(elem)

    db.close()


if __name__ == "__main__":
    filter_func()
