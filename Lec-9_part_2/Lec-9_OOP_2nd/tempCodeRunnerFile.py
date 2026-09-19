class Student:

    # Class variable
    school = "ABC College"

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

    # Instance method
    def show_student(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("School:", Student.school)

    # Class method
    @classmethod
    def change_school(cls, new_school):
        cls.new_school = new_school


student1 = Student("Sudip", 21)
student2 = Student("Ram", 22)

student1.show_student()
student2.show_student()

# Calling class method
Student.change_school("KU")

print("\nAfter changing school:")

student1.show_student()
student2.show_student()