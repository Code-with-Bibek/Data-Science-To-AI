# super() is used in a child class to access methods or the __init__() method of its parent class.

'''
Create a Vehicle parent class with brand and year attributes.
Create a Car child class that inherits from Vehicle and adds model, fuel_type, and price.
Use super().__init__() to initialize the parent class attributes

'''

class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

        print("Vehicle initialized")


class Car(Vehicle):
    def __init__(self, brand, year, model, fuel_type, price):
        super().__init__(brand, year)

        self.model = model
        self.fuel_type = fuel_type
        self.price = price

        print("Car initialized")


car1 = Car("Toyota", 2025, "Camry", "Petrol", 4500000)

print(car1.brand)
print(car1.year)
print(car1.model)
print(car1.fuel_type)
print(car1.price)