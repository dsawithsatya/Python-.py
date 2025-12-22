# import pymysql.connector 
# try:
#     y="create table company(eid int,ename varchar,sal int,company varchar)"
#     con=pymysql.connecter.connect(host="localhost",user='root',password='',database="satya")
#     cursor=con.cursor()
#     cursor.execute(y)
#     print("Created the table")
    
# except BaseException:
#     if con:
#         con.rollback()
#     print("Try to check the error is : ",BaseException)
# finally:
#     if cursor:
#         cursor.close()
    
#     elif con:
#         con.close()

from mysql.connector import *
x=connect(user='root',password="903266",database='abc')
y=x.cursor()
y.execute('select name from emp where name="satya"')
y.close()
x.close()