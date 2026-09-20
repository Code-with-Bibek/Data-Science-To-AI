'''
Write a python program where the python compiler itself generate a random number between the range of user input.

and we ask the user to guess a number between the range..
if the guessed number is exact,print you guessed it right
if less than the target number,print you guessed it low
if higher then the target number,print you guess it high

'''

import random
a = int(input("Enter the lowest range:"))
b = int(input("Enter the highest range:"))

target = random.randint(a,b)

while True:
    guess = int(input(f"Try Guessing a number betn {a} and {b}"))

    if(guess == target):
        print("You guessed it right!")
        break
    elif(guess < target):
        print("You guessed it low!")
        
    elif(guess > target):
        print("You guessed it high")
        
    else:
        print("Invalid guess!")
    