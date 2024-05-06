#!/usr/bin/python3
"""
    A better query to prevent sql injections
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

    query = "SELECT * FROM states WHERE BINARY states.name = %s"
    cur.execute(query, (state,))

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
