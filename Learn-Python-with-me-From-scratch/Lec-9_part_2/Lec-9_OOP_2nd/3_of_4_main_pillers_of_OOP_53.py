'''
simply , inheritaing all the properties of parent class to child class

'''

class car :
    colour = "Blue"
    # @staticmethod
    def start(self):
        print("Car started!!")

    # @staticmethod
    def stop(self):
        print("car stopped!!!")

class BMW(car):   # Inherit the properties of class car 
    def __init__(self, model):
        self.model = model

car1 = BMW("M4")
print(car1.model)

car2 = BMW("M2")
print(car2.model)

print(car1.colour)
print(car1.start())



