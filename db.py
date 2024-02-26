import sqlite3

connection=sqlite3.connect("books.sqlite")

Create_table= "CREATE Table if not exists Books (ID INTEGER PRIMARY KEY, TITLE TEXT  NOT NULL, AUTHOR TEXT NOT NULL)"
cursor = connection.cursor()
cursor.execute(Create_table)
print("created table successfully")