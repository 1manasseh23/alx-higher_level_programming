#!/usr/bin/python3

import mysql.connector

# Establish a database connection
db_connection = mysql.connector.connect(
  host="abednego",
  user="1manasseh23",
  passwd="12345",
  database="hbtn_0e_0_usa"
)

# Create a cursor object
cursor = db_connection.cursor()

# Execute the SQL query
cursor.execute("SELECT * FROM states")

# Fetch the results
records = cursor.fetchall()

for record in records:
    print(record)

# Close the connection
db_connection.close()
