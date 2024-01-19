#!/usr/bin/python3
""" Connecting to my local database and list staes in that database """
import MySQLdb
import sys

if __name__ == "__main__":
    try:
        mydb = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            database=sys.argv[3],
            charset="utf8",
        )
        mycursor = mydb.cursor()
        sql = "SELECT cities.name \
            FROM cities \
            JOIN states ON cities.state_id = states.id \
            WHERE BINARY states.name = %s \
            ORDER BY cities.id;"

        mycursor.execute(sql, (sys.argv[4],))

        querry = mycursor.fetchall()
        len_query = len(querry)

        row = 0
        if (querry):
            for row in range(len_query):
                if (row == (len_query - 1)):
                    print(querry[row][0])
                else:
                    print(querry[row][0], end=", ")
        else:
            print()

        mycursor.close()
        mydb.close()
    except Exception as e:
        print()
