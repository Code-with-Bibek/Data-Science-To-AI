'''
Take a number from the user and calculate the sum of all its digits.

For example:

Input: 5832
Output: 18

'''

a = int(input("Enter a number to be sumed off :"))
sum = 0
while ( a != 0 ):

    sum = sum + (a%10)
    a = a // 10

print(sum)