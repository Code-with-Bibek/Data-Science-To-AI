#Wap to input two integer numbers a & b ..
#Print True if a is greater than or equals to b ..otherwise False

a = int(input("Enter a number:"))
b = int(input("Enter another number:"))
if(a>=b):
    print("True")
else:
    print("False")

# #or

a = int(input("Enter a number:"))
b = int(input("Enter another number:"))
print(a >= b)

#or if the question asked us like this : #Wap to input integers n Print the number which is the greatest among all 

a = int(input("Enter how many number you want to print :"))
largest = int(input("Enter integer 1 :"))

for i in range(1 , a):
    b = int(input(f"Enter the integer {i + 1}: "))

    if b > largest:
        largest = b
print("The largest is :" , largest)




