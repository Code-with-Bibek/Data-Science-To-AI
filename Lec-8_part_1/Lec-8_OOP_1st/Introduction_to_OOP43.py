# classes , instructor , objects , static methods

'''
a = 28
b = 45

sum = a+b      these are how we do before ..this is called procedural programming
print(sum)

diff = a-b
print(diff)

'''

# then functional programming ma shift bhaim..that increases the reusuability of the code and remove redundant data
# now we study OOP..

# class is the blueprint for creating objects

class student :    # Class
    name = "bibek"

s1 = student()   # object
print(s1.name)

s2 = student()    # object
print(s2.name)


class factory :
    workerName = "BIbek Lamivhhane" , "sudip lamichane" , "crystal lamichhane"
    utensils = "karchula" , "spoon" , "dadu"

fac1 = factory()
print(fac1.workerName)