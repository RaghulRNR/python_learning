import mysql.connector

try:

    con=mysql.connector.connect(user='root',
                                password='root',
                                host='localhost')
    cur=con.cursor()
    query="create database Test1"
    cur.execute(query)
    print('Database created successfully')
    con.commit()
except mysql.connector.Error as err:
    con.rollback()
    print('Database Error=', err)
finally:
    if cur:
        cur.close()
    if con:
        con.close()