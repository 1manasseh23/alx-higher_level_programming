#!/usr/bin/python3
"""
This  script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials from command line arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MySQL server
    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username,
                             passwd=password, db=db_name, charset="utf8")
        cursor = db.cursor()

        # Execute query to retrieve states
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        rows = cursor.fetchall()

        for row in rows:
            print(row)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
