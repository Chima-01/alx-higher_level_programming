#!/usr/bin/python3
import MySQLdb

mydb = MySQLdb.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="root",
    database="hbtn_0e_0_usa",
    charset="utf8",
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM states")
querry = mycursor.fetchall()

for row in querry:
    print(row)


mycursor.close()
mydb.close()
