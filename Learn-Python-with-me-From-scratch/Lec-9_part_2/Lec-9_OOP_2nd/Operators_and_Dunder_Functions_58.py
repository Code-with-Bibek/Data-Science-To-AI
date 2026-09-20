'''
we use  like + , - , * , /

# for example :

print(19 + 45) # This is an integer
print("Bibek" + "Lamichhane")  # This is an string and it concatinates
print([3,4,6,7] + [7,8,0,4])   # this is an list and it merges

means : + operator has many meaning on different scenarios

Dunder methods allow Python objects to define how special operations such as +, -, *, /, comparisons, printing, etc. 
should behave.

but , we normally use them for complex numeber calculations

'''


# some dunder functions are : A)  a.__add__(b)
#                             B)  a.__sub__(b)
#                             C)  a.__truediv__(b)
#                             D)  a.__mul__(b)
#                             E)  a.__mod__(b)


a = 34
b = 23
print(a.__add__(b))  # a + b
print(a.__sub__(b))  # a - b
print(a.__mul__(b))  # a * b
print(a.__mod__(b))  # a % b
print(a.__truediv__(b))  # a / b

# example :

class student :
    def __init__(self, num1):
        self.num1 = num1
    def __add__(self, other):
        return self.num1 + other.num1
s1 = student(45)
s2 = student(67)
print(s1 + s2)