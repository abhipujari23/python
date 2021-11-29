from dbconn import *

person2 = Persons("Bob", "Davis", 23)

c.execute("""INSERT INTO persons VALUES
    ('{}','{}','{}')""".format(person2.first, person2.last, person2.age))

commit()
close()