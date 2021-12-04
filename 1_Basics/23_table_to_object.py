#to make communication easier we create persons class that has column as attributes
import sqlite3

class Persons():
    def __init__(self, first = None, last = None, age = None):
        self.first = first
        self.last = last
        self.age = age

    def clone_person(self, result):
        self.first = result[0]
        self.last = result[1]
        self.age = result[2]

conn = sqlite3.connect('mydata.db')
c = conn.cursor()

c.execute("""SELECT * FROM persons WHERE last_name = 'Smith'""")

#creating Persons Object
person1 = Persons()
person1.clone_person(c.fetchone())

conn.close()

#printing individual values
print("First Name: {} \nLast Name: {} \nAge: {}".format(person1.first, person1.last, person1.age))