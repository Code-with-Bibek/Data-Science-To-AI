# WAP to check a user entered number is odd or even

num = int(input("Enter a number to check for odd or even :"))
if num %2 == 0:
    print(f"The number {num} is even.")
else :
    print(f"The number {num} is odd.")  



# or

a = int(input("Enter how many numbers you wanna check: "))

count_even = 0
count_odd = 0
for i in range(a):
    check = int(input(f"Enter the {i + 1} number :"))
    if check % 2 == 0:
        print(f"The number {check} is even.")
        count_even += 1
    else:
        print(f"The number {check} is odd.")
        count_odd += 1

print("Number of even numbers:", count_even)
print("Number of odd numbers:", count_odd)  
  





