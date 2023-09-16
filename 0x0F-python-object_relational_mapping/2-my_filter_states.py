#!/usr/bin/python3
""" Connecting to my local databases
list al tables that matches a particular argument"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) == 5:
        mydb = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            database=sys.argv[3],
            charset="utf8",
        )

        mycursor = mydb.cursor()
        sql = "SELECT * FROM states WHERE name = %s ORDER BY states.id;"
        mycursor.execute(sql, (sys.argv[4],))

        querry = mycursor.fetchall()

        for row in querry:
            print(row)

        mycursor.close()
        mydb.close()
