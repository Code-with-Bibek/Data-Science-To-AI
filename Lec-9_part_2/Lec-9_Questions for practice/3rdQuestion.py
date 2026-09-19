# WAP to take input from user of marks of three subjects..print the percentage and grade using @property . program should ask user for marks 
# program should ask user for marks input.


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
        return total / 3

    @property
    def grade(self):
        percentage = self.percentage

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


while True:
    physics = float(input("Enter Physics marks: "))

    if 0 <= physics <= 100:
        break
    else:
        print("Invalid marks! Enter marks between 0 and 100.")


while True:
    chemistry = float(input("Enter Chemistry marks: "))

    if 0 <= chemistry <= 100:
        break
    else:
        print("Invalid marks! Enter marks between 0 and 100.")


while True:
    maths = float(input("Enter Maths marks: "))

    if 0 <= maths <= 100:
        break
    else:
        print("Invalid marks! Enter marks between 0 and 100.")


# Create student object
s1 = Student(physics, chemistry, maths)


# Display result

print("Physics   :", s1.physics)
print("Chemistry :", s1.chemistry)
print("Maths     :", s1.maths)

print("Total     :", s1.total_marks(), "/ 300")
print("Percentage:", s1.percentage, "%")
print("Grade     :", s1.grade)