import mysql.connector
try:
    con=mysql.connector.connect(user='root',
                                password='root',
                                host='localhost',
                                database='employees')
    cur=con.cursor()
    query="insert into employees values(name,address,salary,eno) values(%s,%s,%s,%s)"
    records = [( 'sunny', 'Mumbai',2000, 200),
               ( 'Bunny', 'Hyd ',3000, 300),
               ( 'Chinny', 'Hyd',4000, 400)]
    cur.executemany(query, records)
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