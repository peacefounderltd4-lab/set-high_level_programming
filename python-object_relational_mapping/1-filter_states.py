#!/usr/bin/python3
"""Lists all states from the database that match a given name."""

import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()
    cursor.execute(
        "SELECT id, name FROM states WHERE name = %s "
        "ORDER BY id ASC",
        (state_name,)
    )

    for state in cursor.fetchall():
        print(state)

    cursor.close()
    db.close()
