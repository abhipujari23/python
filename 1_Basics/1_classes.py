#creating class

class Car:

    #global class variable #variable value does not change for different objects
    amount_cars = 0

    #__init__ is used to initialize a class
    #parameter self is mandatory, atleast this parameter is required
    def __init__(self, manufacturer, model, hp): 
        #hidden variable, used to create variable that can only be accessed with the class
        self.__hidden = "Hello"
        print(self.__hidden)

        self.manufacturer = manufacturer
        self.model = model
        self.hp = hp
        #using global class variable to keep note of objects
        Car.amount_cars += 1

#adding function
    def print_info(self):
        print(("Manufacturer: {} \nModel: {} \nHP: {}").format(self.manufacturer, self.model, self.hp))

    def print_car_amount(self):
        print(("Total Cars: {}").format(Car.amount_cars))

#creating object

mycar1 = Car("Tesla", "Model X", 525)
mycar1.print_info()
mycar1.print_car_amount()