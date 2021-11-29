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

def commit():
    conn.commit()

def close():
    conn.close()