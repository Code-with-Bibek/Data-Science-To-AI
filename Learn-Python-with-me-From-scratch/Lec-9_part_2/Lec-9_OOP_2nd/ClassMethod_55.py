# ============================================================
# CLASS METHOD IN PYTHON
# ============================================================

# A class method is a method that works with the CLASS
# rather than a particular OBJECT.
#
# We create a class method using the @classmethod decorator.
#
# The first parameter of a class method is "cls".
# "cls" refers to the CLASS itself.
#
# self -> refers to the current OBJECT
# cls  -> refers to the current CLASS


# ------------------------------------------------------------
# BASIC EXAMPLE
# ------------------------------------------------------------

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
        cls.school = new_school


student1 = Student("Sudip", 21)
student2 = Student("Ram", 22)

student1.show_student()
student2.show_student()

# Calling class method
Student.change_school("KU")

print("\nAfter changing school:")

student1.show_student()
student2.show_student()


# ------------------------------------------------------------
# HOW IT WORKS
# ------------------------------------------------------------

# When we write:
#
# Student.change_school("XYZ College")
#
# Python understands:
#
# cls = Student
#
# Therefore:
#
# cls.school = new_school
#
# is basically:
#
# Student.school = "XYZ College"


# ------------------------------------------------------------
# IMPORTANT DIFFERENCE
# ------------------------------------------------------------

# Instance method:
#
# def method(self):
#     ...
#
# self -> object


# Class method:
#
# @classmethod
# def method(cls):
#     ...
#
# cls -> class


# ------------------------------------------------------------
# WHY USE CLASS METHODS?
# ------------------------------------------------------------

# Class methods are useful when we need to:
#
# 1. Access class variables
# 2. Modify class variables
# 3. Create alternative constructors


# ------------------------------------------------------------
# ALTERNATIVE CONSTRUCTOR
# ------------------------------------------------------------

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):

        name, age = data.split("-")

        return cls(name, int(age))


# Normal way of creating an object:
student1 = Student("Sudip", 21)

# Another way of creating the same type of object:
student2 = Student.from_string("Ram-22")

print(student1.name, student1.age)
print(student2.name, student2.age)


# Here:
#
# cls = Student
#
# Therefore:
#
# return cls(name, int(age))
#
# is basically:
#
# return Student(name, int(age))
#
# So the class method can be used as an
# ALTERNATIVE CONSTRUCTOR.


# ============================================================
# KEY POINT TO REMEMBER
# ============================================================

# self -> current OBJECT
# cls  -> current CLASS
#
# Instance method -> works with object
# Class method    -> works with class
#
# @classmethod tells Python that the method
# should receive the class as its first argument.