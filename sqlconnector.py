import mysql.connector
spcdatabase = mysql.connector.connect( # just giving a name to my connection
    host="localhost", # as you can see in select USER() command
    user="root",
    password="    "
    )
spccur=spcdatabase.cursor() # cursor() method is called by the connection again stored in spccur 
spccur.execute("show databases")
for i in spccur:
    print(i)