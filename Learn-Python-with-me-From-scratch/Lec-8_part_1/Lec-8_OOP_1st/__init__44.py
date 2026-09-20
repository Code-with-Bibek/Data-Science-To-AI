#  is an constructor who always takes an argument...and that is "self"

class student :

    # Default constructor --> we can also make it but not necessary to make..python automatically creates it by default
    def (self):
        pass

    # Parametarized constructor --> got parameters along with self
    def (self , fullname , roll_no , address , standard ) :
        self.fullname = fullname           # object bhitra new fullname create hune wala xa
        self.roll_no = roll_no             #not necessarly we say self...but every programmer use self..so we will use self
        self.address = address
        self.standard = standard

s1 = student("Bibek lamichhane" , 8 , "dhalpa" , "Bachelors")   # We have to pass 4 required arguments
print(s1.address) 
print(s1.fullname) 
print(s1.roll_no , s1.address) 
print(s1.standard) 

# We can also store this class object realtion in list , string , dictionary..not necessary using OOP..
#But in most of the scenarios , OOP is used
