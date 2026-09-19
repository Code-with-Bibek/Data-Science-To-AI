'''

2) Encapsulation --> Encapsulation is about protecting data inside a class.

It means keeping data (properties) and methods together in a class, while controlling how the data can be accessed from outside the class.

This prevents accidental changes to your data and hides the internal details of how your class works. 

'''

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

s1 = Student("Bibek" , (56,23,89))
print(s1.average())
        # Student
        # │
        # ├── name
        # ├── marks      # name , marks and average() are packed inside same class....And that is encapsulation
        # │
        # └── average()