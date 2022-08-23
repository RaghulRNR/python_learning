import mysql.connector

try:
    con=mysql.connector.connect(user='root',
                                password='root',
                                host='localhost',
                                database="employees")
    query="DROP database employees"
    cur=con.cursor()
    cur.execute(query)
    print('Query executed successfully')
except mysql.connector.Error as err:
    con.rollback()
    print(err)
finally:
    if cur:
        cur.close()
    if con:
        con.close()
