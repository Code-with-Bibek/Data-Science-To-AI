'''
any data / variable (name,marks,address,etc) --> attribute

class.attr
obj.attr


if some parameter is commom on every object , we define it before __init__ constructor

'''
# lets suppoose school name is common on a class object :

class student :
    school_name = "SMS"   #school name is common on all object to be created below..so , we need to define it once
    def __init__(self, name , standard , roll_no):
        self.name = name
        self.standard = standard
        self.roll_no = roll_no
s1 = student("bibek lamichhane" , 12 , 8)
print(s1.roll_no)
print(s1.name , s1.school_name)
print(student.school_name)
# or...this is also valid
# print(student.roll_no)
# print(student.name , s1.school_name)
# print(student.school_name)

s2 = student("sudip sharma" , 11 , 5)
print(s2.roll_no)
print(s2.name , s1.school_name)
print(s2.school_name)

# or...this is also valid
# print(student.roll_no)
# print(student.name , s1.school_name)
# print(student.school_name)

s3 = student("indu sharma" , 13 , 1)
print(s3.roll_no)
print(s3.name , s1.school_name)
print(s3.school_name)
# or...this is also valid
# print(student.roll_no)
# print(student.name , s1.school_name)
# print(student.school_name)