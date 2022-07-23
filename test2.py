import mysql.connector as connection

mydb = connection.connect(host='localhost',user='root',passwd ='mysql')

cursor1 = mydb.cursor()
s = "insert into yash.ineuron values(101, 'yashchavan','yash@gmail', 100)"
cursor1.execute(s)
cursor1.execute(s)
cursor1.execute(s)
cursor1.execute(s)
cursor1.execute(s)
cursor1.execute(s)
cursor1.execute(s)
cursor1.execute(s)
mydb.commit()
cursor1.execute("select * from yash.ineuron")
for i in cursor1.fetchall():
    print(i)