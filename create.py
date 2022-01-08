import sqlite3
connection=sqlite3.connect('data.db')
cursor=connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS USERS (ID INTEGER PRIMARY KEY,USERNAME TEXT,PASSWORD TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS ITEMS (ID INTEGER PRIMARY KEY,NAME TEXT,PRICE REAL)")
'''cursor.execute("INSERT INTO ITEMS VALUES (?,?)",('Chair',20.99))

select="select * from ITEMS"
for row in cursor.execute(select):
    print(row)
'''
connection.commit()
connection.close()
