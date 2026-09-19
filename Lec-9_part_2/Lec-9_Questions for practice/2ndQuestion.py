# calculate the percentage of the student which is the class itself and takes 3 arguments ; physics , chemistry and maths

# class student :
#     def __init__(self, phy , chem , math) :
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#         self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

    
# s1 = student(45,56,34)
# print(s1.percentage)  # not a problem to print

# # if we thought of changing the marks of physics to 87 , then we can easily
# s1.phy = 87
# print(s1.phy)
# print(s1.percentage)  # you can see in the terminal , the percentage is still the same after we changed the marks of physics to 87
# # purano hisab le set bhako xa...automatically change bhako xaina



# # to make the result change after changing the marks value later on ,  we use property decorator

# class student :
#     def __init__(self, physics , chemistry , maths):
#         self.physics = physics
#         self.chemistry = chemistry
#         self.maths = maths

#     @property
#     def percentage(self):
#         return str((self.physics + self.chemistry + self.maths) / 3) + "%"

# s1 = student(45,56,34)
# print(s1.percentage)

# # if we thought of changing the marks of physics to 87 , then we can easily
# s1.physics = 87
# print(s1.percentage)

# with using shutter :

class Student:

    def __init__(self, physics, chemistry, maths):
        self.physics = physics
        self.chemistry = chemistry
        self.maths = maths

    def total_marks(self):
        return self.physics + self.chemistry + self.maths

    @property
    def percentage(self):
        total = self.total_marks()

        if 0 <= total <= 300:
            return total / 3
        else:
            return "Invalid marks!"

    @property
    def grade(self):
        percentage = self.percentage

        if isinstance(percentage, str):
            return "Invalid"

        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B+"
        elif percentage >= 60:
            return "B"
        elif percentage >= 50:
            return "C+"
        elif percentage >= 40:
            return "C"
        else:
            return "F"


s1 = Student(34, 56, 78)

print("Total:", s1.total_marks())
print("Percentage:", s1.percentage, "%")
print("Grade:", s1.grade)