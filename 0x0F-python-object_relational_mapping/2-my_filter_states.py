#!/usr/bin/python3
""" Connecting to my local database and list staes in that database """
import MySQLdb
import sys

if __name__ == "__main__":
    if sys.rgv[4]:
        mydb = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            database=sys.argv[3],
            charset="utf8",
        )
        mycursor = mydb.cursor()

        sql = "SELECT * FROM states WHERE name = '{}' ORDER BY states.id;\
                ".format(
            sys.argv[4]
        )
        mycursor.execute(sql)

        querry = mycursor.fetchall()

        for row in querry:
            print(row)

        mycursor.close()
        mydb.close()
