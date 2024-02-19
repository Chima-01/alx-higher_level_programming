#!/usr/bin/python3
import MySQLdb
import sys
""" Intro to mysqldb """

username, password, database, state_name = sys.argv[1:5]
conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
)

cur = conn.cursor()
query = "SELECT * FROM states WHERE name={} ORDER BY states.id ASC".format(state_name)
cur.execute(query)
query_rows = cur.fetchall()

for row in query_rows:
    print(row)

cur.close()
conn.close()
