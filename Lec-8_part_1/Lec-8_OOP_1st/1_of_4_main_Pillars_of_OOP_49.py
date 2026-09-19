'''
1) Abstraction --> Abstraction means showing only what the user needs and hiding the complicated implementation.

Think about your phone.

You press:

📞 Call

You don't need to know:

how the phone connects to the tower
how signals are converted
how packets travel
how the network finds the other phone

You just use the simple interface:
Call("Ram")


2) Encapsulation --> 

3) Inheritance --> SEE IN LEC 9

4) Polymorphism --> SEE IN LEC 9

'''

class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

s1 = student("Bibek" , (34,56,65))      
print(s1.marks)
print(s1.name)

print(s1.average())