#!/usr/bin/python3
""""
This a script that takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument
"""
import MySQLdb
import sys


def main():
    # Unpack the arguments provided
    mysql_username, mysql_password, database_name,
    state_name_searched = sys.argv[1:]

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                         passwd=mysql_password, db=database_name)
    cur = db.cursor()

    # Create the SQL query, using format to insert the user input
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    # Execute the query
    cur.execute(query, (state_name_searched,))

    # Fetch all the results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close all cursors and the database connection
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
