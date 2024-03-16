#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa for a given state.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:]

    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password, db=database)
        cursor = db.cursor()

        # Execute query (safe from SQL injection)
        cursor.execute("SELECT cities.name FROM cities \
                        JOIN states ON cities.state_id = states.id \
                        WHERE states.name = %s \
                        ORDER BY cities.id ASC", (state_name,))
        results = cursor.fetchall()

        # Display results
        cities = [row[0] for row in results]
        print(", ".join(cities))

        # Close cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL: {}".format(e))
        sys.exit(1)
