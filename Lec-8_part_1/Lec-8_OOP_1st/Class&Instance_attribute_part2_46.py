class student :
    school_name = "SMS"
    name = "ANY"    # This is an class attribute

    def __init__(self, name , standard , roll_no):
        self.name = name   # This is an object attribute
        self.standard = standard
        self.roll_no = roll_no

# The precedence of object attr > class attr

s1 = student("bibek lamichhane" , 12 , 8)
print(s1.roll_no)
print(s1.name , s1.school_name)  # name will be --> bibek lamichhane

print(student.school_name)
print(s1.name)  # name will be --> bibek lamichhane
