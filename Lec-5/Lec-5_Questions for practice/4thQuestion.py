# Wap to print a multiplication table of a number n

a = int(input("Enter a number n which you wanna take multiplication of :"))
print(f"The multiplication table of {a} is : ")
i = 1
while i <= 10 :
    b = a * i
    print(f"{a} * {i} = " , b )                  
    i += 1


# or 

while True:
    a = int(input("Enter a number n which you wanna take multiplication of: "))

    if a > 0:
        break
    else:
        print("Error! Please enter a positive number.")

i = 1
print(f"The multiplication table of {a} is:")

while i <= 10:
    print(f"{a} * {i} = {a * i}")
    i += 1

    
'''
a * 1 = ....
a * 2 = ....
a * 3 = ....
a * 4 = ....
a * 5 = ....
a * 6 = ....
a * 7 = ....
a * 8 = ....
a * 9 = ....
a * 10 = ....
'''