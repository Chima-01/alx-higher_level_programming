#!/usr/bin/python3
"""
    A script that lists all cities from the database
    hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username, password, database = sys.argv[1:4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8",
    )
    cur = conn.cursor()

    query = "SELECT cities.id, cities.name, states.name FROM cities \
            INNER JOIN states ON states.id = cities.state_id \
            ORDER BY cities.id Asc"
    cur.execute(query)

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
