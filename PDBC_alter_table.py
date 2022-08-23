import mysql.connector

try:
    con=mysql.connector.connect(user='root',
                                password='root',
                                host='localhost',
                                database='employees')
    cur=con.cursor()
    query="Alter Table employees add eno varchar(255);"
    cur.execute(query)
    con.commit()
    print('Record inseted succesfully')
except mysql.connector.Error as err:
    con.rollback()
    print(err)
finally:
    if cur:
        cur.close()
    if con:
        con.close()