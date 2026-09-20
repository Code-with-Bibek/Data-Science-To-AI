# WAP to find the factorial of a number n ..do using for loop

# Using while loop

fact = 1

while True:
    num = int(input("Enter a number to find its factorial: "))

    if num > 0:
        break
    else:
        print("Invalid number. Try again!")

for i in range(1, num + 1):
    fact *= i

print(f"The factorial of {num} is {fact}")

# Using for loop

fact = 1

while True:
    num = int(input("Enter a number to find its factorial: "))

    if num > 0:
        break
    else:
        print("Invalid number. Try again!")

for i in range(1, num + 1):
    fact *= i

print(f"The factorial of {num} is {fact}")

# or even simpler ( for loop)

n = int(input("ENter a number :"))
fact = 1
for i in range(1,n+1):
    fact *= i
print ( fact)

# or using while loop simply

n = int(input("Enter a number :"))
fact = 1
i = 1 
while i <= n :
    fact *= i
    i += 1
print(fact)