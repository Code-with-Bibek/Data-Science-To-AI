'''
Take an integer from the user and determine whether it is even or odd.

But there's a catch:

Do not use %.

'''

a = int(input("Enter a number "))

if (a == (a//2) * 2) :
    print("Even")
else :
    print("false")


# for 10 : 10//2 == 5*2 ==10 ...so , 10 == 10 True

