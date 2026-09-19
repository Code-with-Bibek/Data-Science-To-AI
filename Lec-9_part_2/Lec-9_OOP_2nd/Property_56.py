'''
Normal method:
student1.result()

Property:
student1.result

'''

# @property allows us to access a METHOD like an ATTRIBUTE.
#
# Normal method:
#
# object.method()
#
# Property:
#
# object.property
#
# We do not use () with a property.

# example :

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property
    def area(self):
        return self.length * self.width


r = Rectangle(10, 5)

print(r.area)


# r.area looks like an attribute,
# but Python actually runs the area() method
# because it has the @property decorator.


# ------------------------------------------------------------
# PROPERTY + ENCAPSULATION
# ------------------------------------------------------------

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance


account = BankAccount(50000)

print(account.balance)


# @property allows us to read the private
# attribute through a controlled interface.


# ------------------------------------------------------------
# PROPERTY WITH SETTER
# ------------------------------------------------------------

class Student:

    def __init__(self, name, marks):
        self.name = name
        self._marks = marks

    # GETTER
    @property
    def marks(self):
        return self._marks

    # SETTER
    @marks.setter
    def marks(self, value):

        if value < 0 or value > 100:
            print("Invalid marks!")
        else:
            self._marks = value


student1 = Student("Sudip", 80)

# Getter is called
print(student1.marks)

# Setter is called
student1.marks = 90

print(student1.marks)

# Setter validates the value
student1.marks = 150


# ============================================================
# KEY POINTS
# ============================================================

# @property
# -> allows a method to be accessed like an attribute.
#
# @property method
# -> GETTER (controls reading)
#
# @property_name.setter
# -> SETTER (controls changing/writing)
#
# self._variable
# -> commonly used as the internal storage variable.
#
#
# Simple memory:
#
# @property       -> GET
# @name.setter    -> SET
#
# self            -> current object
# cls             -> current classj