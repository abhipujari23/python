#when a class inherits other it can overwrite its method

class Animal:

    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Some sound!")

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)

    def make_sound(self):
        print("Bark!")

a1 = Animal("doggo")
a1.make_sound()

d1 = Dog("Dog Mike")
d1.make_sound()