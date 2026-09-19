# WAP to find the number among 3 numbers entered by the users

# a = int(input("Enter a First number you wanna check :"))
# b = int(input("Enter a second number you wanna check :"))
# c = int(input("Enter a third number you wanna check :"))
# if a >= b and a >= c:
#     print(f"{a} is the largest")
# elif b >= a and b >= c:
#     print(f"{b} is the largest")
# else:
#     print(f"{c} is the largest")



# or

a = int(input("Enter the first number :"))
b = int(input("Enter the second number :"))
c = int(input("Enter the  third number :"))
largest = a if a>=b and a>=c else b if b>=c else c
print("The largest one is :" , largest)
