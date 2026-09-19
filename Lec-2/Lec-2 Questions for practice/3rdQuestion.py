#Write a Python program that asks the user how many students are in a class. Then ask for each student's marks (out of 100). Display whether the student has Failed, Passed, Excellent, or Outstanding. Finally, print the number of Outstanding students.

num = int(input("Enter how many subjects you want to input marks for: "))

total = 0
out = 0

for i in range(num):
    marks = int(input(f"Enter marks for subject {i + 1}: "))
    total += marks

average = total / num

print("Total marks:", total)
print("Average:", average)

if average < 50:
    print("Failed badly")
elif average < 80:
    print("Pass but not good marks")
elif average < 90:
    print("Excellent")
elif average <= 100:
    print("Outstanding")
    out += 1
else:
    print("Invalid marks")

print("The numbe of outstanding students are :" , out)

# for counting , we have to make a variable count and set it to 0 .. Then at outstanding elif , we will write count += 1

# num_students = int(input("Enter the number of students: "))

# outstanding_count = 0

# for i in range(num_students):
#     marks = int(input(f"Enter marks of student {i + 1}: "))

#     if marks < 50:
#         print("Failed")
#     elif marks < 80:
#         print("Pass")
#     elif marks < 90:
#         print("Excellent")
#     elif marks <= 100:
#         print("Outstanding")
#         outstanding_count += 1
#     else:
#         print("Invalid marks")

# print("\nNumber of Outstanding students:", outstanding_count)