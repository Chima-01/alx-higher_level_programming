#!/usr/bin/python3
import MySQLdb
import sys
""" Intro to mysqldb """

username, password, database = sys.argv[1:4]
conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
)

cur = conn.cursor()
cur.execute("""SELECT * FROM states WHERE name LIKE 'N%'
        ORDER BY states.id ASC""")
query_rows = cur.fetchall()

for row in query_rows:
    print(row)

cur.close()
conn.close()
