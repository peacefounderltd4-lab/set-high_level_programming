#!/usr/bin/python3
"""
Module that connects to a MySQL database and retrieves all states
ordered by id from the database hbtn_0e_0_usa.
"""
import sys
import MySQLdb


def get_all_states(username, password, database):
    """
    Connects to localhost at port 3306 and prints all states
    sorted in ascending order by states.id.
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    
    rows = cursor.fetchall()
    for row in rows:
        print(row)
        
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        get_all_states(sys.argv[1], sys.argv[2], sys.argv[3])
        
