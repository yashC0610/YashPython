import mysql.connector as conn

mydb= conn.connect(host='localhost',user='root',passwd='mysql')

cursor=mydb.cursor()

cursor.execute("show databases")

print(cursor.fetchall())

#cursor.execute("create database TATA")

#cursor.execute("create table TATA.Emp(Emp_name varchar(80), Emp_age int)")

s= "insert into TATA.Emp alues('YashChavan',10)"

cursor.execute(s)
mydb.commit()

cursor.execute("select * from TATA.Emp")

print(cursor.fetchall())