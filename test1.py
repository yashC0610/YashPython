import mysql.connector as connection

mydb = connection.connect(host='localhost',user='root',passwd ='mysql')

cursor1 = mydb.cursor()

#q1= cursor1.execute("create table yash.ineuron(emp_id int(10), emp_name varchar(80), emp_mail varchar(10), emp_salary int(7))")

q2= cursor1.execute("select * from yash.ineuron")

print(q2)