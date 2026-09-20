'''
Ask the user for a number and print:

1 * number
2 * number
.
.
.
10 * number

'''

a = int(input("Enter a number :"))
for i in range(1,10):
    print(i ,"*", a)