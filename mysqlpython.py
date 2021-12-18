#!/usr/bin/python3

import mysql.connector

mydb = mysql.connector.connect(
   user='root',
   password='sercet',
   host='localhost',
   database='test'
)

#cnx.close()

mycursor = mydb.cursor()
#get into mysql db and execute the TABLE
mycursor.execute("SELECT * FROM bar")

myresult = mycursor.fetchall()
#print all the values from Table of DB to screen
print ('Total numbers of your Table: ')
for x in myresult:
  print(x)

