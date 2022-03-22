import mysql.connector

spcdatabase=mysql.connector.connect(
    host='localhost',
    user='root',
    password='    ',
    database='rent'
    )

spccur=spcdatabase.cursor()

spccur.execute("show tables")

for i in spccur:
    print(i)