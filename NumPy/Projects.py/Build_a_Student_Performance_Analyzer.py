'''
Your input could look something like:

Enter marks for Student 1:
Enter marks for Student 2:
Enter marks for Student 3:
...

Store the data in NumPy.

Then your program should produce something like:

===== STUDENT PERFORMANCE =====

Total Students: 5

Average Mark: 74.6
Highest Mark: 95
Lowest Mark: 51

Students Passed: 4
Students Failed: 1

Overall Performance: Good

'''

print("----For average----")
def average_mark():

    for i in range(a):
        total = 0
        num = int(input(f"Enter the marks of the {i + 1} student :"))
        total += num

    avg = total/a
    return avg

a = int(input("Enter how many students we are talking?:"))

average = average_mark()

print("----For appending into a list----")
import numpy as np
nums_store = []
for i in range(a):
    num = int(input(f"Enter the marks of {i+1} student :"))
    nums_store.append(num)

print("----For pass----")
def pass_count():
    count = 0
    for i in range(a):
        number = int(input(f"Enter marks of {i + 1} student"))
        if(number >= 40):
            count += 1
    return count
count = pass_count()

print("----For fail----")
def fail_count():
    count = 0
    for i in range(a):
        number = int(input(f"Enter marks of {i + 1} student"))
        if(number < 40):
            count += 1
    return count
count_fail = fail_count()

print("----For performance check----")
def performance_checker():
    count = 0

    for i in range(a):
        number = int(input(f"Enter marks of {i + 1} student: "))

        if number >= 40:
            count += 1

    pass_percentage = (count / a) * 100

    if pass_percentage >= 80:
        return "Excellent"
    elif pass_percentage >= 50:
        return "Good"
    else:
        return "Needs Improvement"


checker = performance_checker()

print("=== Student Performance ===")
print("Average mark :",np.mean(nums_store))
print("Highest mark :",np.max(nums_store))
print("Lowest mark :",np.min(nums_store))
print("Student passed :",count)
print("Student failed :",count_fail)
print("The overall performance :",checker)



# or ( AI generated)

import numpy as np




students = int(input("Enter number of students: "))

marks = []

for i in range(students):
    mark = int(input(f"Enter marks for Student {i + 1}: "))
    marks.append(mark)

marks = np.array(marks)




average = np.mean(marks)
highest = np.max(marks)
lowest = np.min(marks)




passed = np.sum(marks >= 40)
failed = np.sum(marks < 40)




pass_percentage = (passed / students) * 100

if pass_percentage >= 80:
    performance = "Excellent"
elif pass_percentage >= 50:
    performance = "Good"
else:
    performance = "Needs Improvement"




print("\n===== STUDENT PERFORMANCE =====")

print(f"\nTotal Students: {students}")

print(f"\nAverage Mark: {average}")
print(f"Highest Mark: {highest}")
print(f"Lowest Mark: {lowest}")

print(f"\nStudents Passed: {passed}")
print(f"Students Failed: {failed}")

print(f"\nOverall Performance: {performance}")



