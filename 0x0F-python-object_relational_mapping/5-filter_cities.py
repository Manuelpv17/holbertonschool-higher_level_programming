#!/usr/bin/python3
"""takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa"""

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
        "SELECT cities.id, cities.name, states.name \
            FROM cities LEFT JOIN states ON cities.state_id \
                = states.id ORDER BY cities.id ASC;")

    r = cursor.fetchall()
    string = ""
    for elem in r:
        if (elem[2] == sys.argv[4]):
            string += elem[1] + ", "
    print(string[:-2])

    db.close()


if __name__ == "__main__":
    filter_func()
