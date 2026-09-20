# WAP to create a student class . and give 2 argument as name and marks of 3 subjects.create a seperate methods to print the average

# class student :
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def sum(self):
#         sum = s1.marks[0]+s1.marks[1]+s1.marks[2]
#         print("The sum is :", sum)
#     def average(self):
#         average = (s1.marks[0]+s1.marks[1]+s1.marks[2])/3

#         print("The average is : " , int(average))

# s1 = student("Bibek" , (34,56,65))      
# print(s1.marks)
# print(s1.name)
# print(s1.sum())
# print(s1.average())

# or we can ask user to give name and marks of student..

class student_details:
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks

    def total(self):
        total = sum(self.marks)
        print("The total marks of", self.name, "is:", total)

    def average(self):
        average = sum(self.marks) / len(self.marks)
        print("The average marks of", self.name, "is:", average)

student = []
a = int(input("How many students?"))
b = int(input("How many subjects?"))
for i in range(a):
    subject = input(f"Enter the name of {i+1} student ")
    student.append(subject)

    marks = []
    for j in range(b):
        while True :
            marks = int(input(f"Enter the marks of {j+1} subject "))
            if (marks > 100 or mark < 0):
                print("Try again ..Not a valid mark..")
                continue
            marks.append(marks)
            break
            
    s = student(name,marks)
    student.append(s)





    
