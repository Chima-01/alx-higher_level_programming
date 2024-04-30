#!/usr/bin/python3
"""
    Display all value in a state that matches an argument
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username, password, database, state_name = sys.argv[1:5]
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8",
    )

    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM states WHERE states.name = '{}' ORDER BY states.id \
                ASC".format(state_name)
    )
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
