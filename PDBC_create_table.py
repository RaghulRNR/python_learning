import mysql.connector

try:
    con=mysql.connector.connect(user='root',
                                password='root',
                                host='localhost',
                                database="employees")
    cur=con.cursor()
    query="create table employees(name VARCHAR(255), address VARCHAR(255));"
    cur.execute(query)
    print('Database created successfully')
except mysql.connector.Error as err:
    con.rollback()
    print('Table  Creation failed',err)
finally:
    if cur:
        cur.close()
    if con:
        con.close()
