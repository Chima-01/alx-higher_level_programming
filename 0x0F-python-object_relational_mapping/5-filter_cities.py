#!/usr/bin/python3
"""
    A script that takes in the name of a state as an argument and lists
    all cities of that state, using the database
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username, password, database, state = sys.argv[1:5]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8",
    )
    cur = conn.cursor()

    query = "SELECT cities.name FROM cities \
            INNER JOIN states ON BINARY states.name = %s \
            WHERE states.id = cities.state_id"
    cur.execute(query, (state,))

    query_rows = cur.fetchall()

    for row in query_rows:
        print(*row, end=' ')
    print()

    cur.close()
    conn.close()
