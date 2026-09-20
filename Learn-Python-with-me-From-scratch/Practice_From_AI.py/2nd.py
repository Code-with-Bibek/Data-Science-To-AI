'''
Take three numbers from the user and print the largest one.

Don't use Python's built-in max().

'''

a = int(input("Enter 1st number :"))
b = int(input("Enter 2ndt number :"))
c = int(input("Enter 3rd number :"))
if(a > b and a > c ):
    print("greatest is :" , a)
elif(b > a and b > c):
    print("greatest is :" , b)
else :
    print("greatest is ", c)

