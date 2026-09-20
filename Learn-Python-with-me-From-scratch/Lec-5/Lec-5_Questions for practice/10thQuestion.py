# WAP to print numbers from 1 to 100 using for and range

for i in range(1,101) :
    print(i)

# WAP to print numbers from 100 to 1 using for and range
for i in range(100,0,-1):
    print(i)

# WAP to print multiplication table of n using for and range
num = int(input("Enter a number :"))
for i in range(1,11):
    print(num*i)
    i += 1