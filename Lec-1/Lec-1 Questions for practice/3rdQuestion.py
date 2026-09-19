# #WAP to input two floating points numbers and find their average

# a = float(input("Enter the first floating number:"))
# b = float(input("Enter the second floating number"))
# Average = (a + b)/2
# print("The average is :", Average)

# # or

# print("Average:",(a+b)/2)

# # or ( by myself )


# a = int(input("Enter how many numbers you want to average:"))

# total = 0.0

# for i in range(a):
#     num = float(input(f"enter the floating number {i + 1}:"))
#     total += num
# average = total / a
# print("The average is :", average)


total = 0.0
b = int(input("Enter how many numbers you want for average:"))
for i in range(b):
    num = int(input(f"Enter the {i + 1} number :"))
    total += num

average = total / b
print("The average is :" , average)


