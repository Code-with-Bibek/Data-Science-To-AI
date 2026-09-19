'''
Create a Person parent class with name, age, and city attributes.
Create a Student child class that inherits from Person and adds college and roll_no. 
Use super().__init__() to initialize the attributes of the parent class. 
Also print a message from both __init__() methods to understand the order of execution.

 '''


class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

        print("Parent class initialized")


class Student(Person):
    def __init__(self, name, age, city, college, roll_no):
        super().__init__(name, age, city)

        self.college = college
        self.roll_no = roll_no

        print("Child class initialized")


student1 = Student("Sudip", 21, "Kathmandu", "TU", 101)

print(student1.name)
print(student1.age)
print(student1.city)
print(student1.college)
print(student1.roll_no)