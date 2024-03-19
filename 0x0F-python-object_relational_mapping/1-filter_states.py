#!/usr/bin/python3
"""
Lists all states with a name starting with 'N' from the database.
"""
import MySQLdb
import sys


def list_states_n(username, password, dbname):
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        list_states_n(sys.argv[1], sys.argv[2], sys.argv[3])
