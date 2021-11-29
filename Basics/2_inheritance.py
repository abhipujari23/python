#Concept of Inheritance


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_older(self, years):
        self.age += years

class Programmer(Person):
    def __init__(self, name, age, language):
        super(Programmer, self).__init__(name, age)

        self.language = language

    def print_language(self):
        print(("Favorite programming language: {}").format(self.language))

p1 = Programmer("Abhishek", 22, "Python")
print(p1.name)
print(p1.age)
print(p1.language)
p1.print_language()
p1.get_older(5)
print(p1.age)