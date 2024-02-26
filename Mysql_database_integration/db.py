import pymysql
# import mysql

'''
Below section will be for integration of mysql database from localhost
connection=mysql.connector.connect(host= "localhost",
database= "RestAPI_db",
user= "root",
password= "root",

)
'''

connection=pymysql.connect(host= "sql6.freesqldatabase.com",
database= "sql6686921",
user= "sql6686921",
password= "cS3TIlvmJu",
charset='utf8mb4',
cursorclass= pymysql.cursors.DictCursor
)

Create_table= "CREATE Table if not exists Books (ID INTEGER PRIMARY KEY, TITLE TEXT  NOT NULL, AUTHOR TEXT NOT NULL)"
cursor = connection.cursor()
cursor.execute(Create_table)
print("created table successfully")
connection.close()
