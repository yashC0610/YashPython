import mysql.connector as connection

mydb = connection.connect(host='localhost',user='root',passwd ='mysql')

cursor1 = mydb.cursor()
l= []
cursor1.execute("select emp_id, emp_mail from yash.ineuron")
for i in cursor1.fetchall():
    l.append(i)
print(l)
print(type(l[0]))

