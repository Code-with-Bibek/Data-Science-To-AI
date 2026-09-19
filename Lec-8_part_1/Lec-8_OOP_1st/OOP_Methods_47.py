'''
Methods are functions that belongs to objects..

'''


class student :
    def __init__(self,name,address,marks) :  # constructor --> init
        self.name = name
        self.address = address
        self.marks = marks

    def hello(self):                 # This is a method --> which only takes self pareameter and uses it on method
        print("Hello")   # I made here a method that says " hello "

    def welcome(self):
        print("Welcome")  # or --> print("welcome" , self.name)

    def get_marks(self):
        return (self.marks)

s1 = student("BIbek" , "dhalpa" , 45)
print(s1.name)
print(s1.address)

print(s1.hello())
print(s1.welcome())
print(s1.get_marks())
