# used to delete object itself or object properties

class student :
    def __init__(self,name):
        self.name = name
s1 = student("bibek")
print(s1.name)
del s1
print(s1)