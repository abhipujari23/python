from dbconn import *

#there is much more secure and elegant way to put the values of our attributes into SQL

person = Persons("Julia", "Johnson", 28)

c.execute("INSERT INTO persons VALUES(?, ?, ?)",(person.first, person.last, person.age))

commit()
close()

#Change values before trying