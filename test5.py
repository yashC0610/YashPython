import mysql.connector as connection

mydb= connection.connect(host='localhost',user='root',passwd ='mysql')

print(mydb)

cursor2= mydb.cursor()

cursor2.execute('show databases')

print(cursor2.fetchall())