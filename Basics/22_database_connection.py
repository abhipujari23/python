#Python has preinstalled database sqlLite
import sqlite3

#To create database file we need connect method
#This command creates new db file and connects it to database
conn = sqlite3.connect('mydata.db')

#To execute SQL commands we need to create cursor
c = conn.cursor()

#creating tables
#execute function is used to write query
c.execute("""CREATE TABLE persons(
    first_name TEXT,
    last_name TEXT,
    age INTEGER
    )""")

#Once query is written to execute we need to commit
conn.commit()


#Inserting Values
c.execute("""INSERT INTO persons VALUES
    ('John','Smith',25),
    ('Anne','Smith',20),
    ('Mike','Johnson',40)""")
conn.commit()


#Selecting Values
c.execute("""SELECT * FROM persons WHERE last_name = 'Smith'""")
#fetchall() function is used to get all the values from the above query
print(c.fetchall())
conn.commit()
#Closing connection
conn.close()