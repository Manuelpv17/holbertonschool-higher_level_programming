#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
import sys


def filter_func():
    """ func """
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
    cursor.execute(
        "SELECT cities.id, cities.name, states.name \
            FROM cities LEFT JOIN states ON cities.state_id \
                = states.id ORDER BY cities.id ASC;")

    r = cursor.fetchall()
    for elem in r:
        print(elem)

    db.close()


if __name__ == "__main__":
    filter_func()
