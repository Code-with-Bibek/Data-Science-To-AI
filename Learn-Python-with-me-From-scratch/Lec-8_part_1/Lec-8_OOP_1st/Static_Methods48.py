'''
while using method before , we must use self parameter..

so in this method , we dont use self..we use @staticmethod

we need to bring it to the class level , instead of object level

'''

class student :
    def __init__(self,name,address,):
        self.name = name
        self.address = address

    @staticmethod    #decorator...which is changing the behaviour of my normal funcn
    def college():
        print("SMS , TU")

s1 = student("bibek" , "dhalpa")
print(s1.college())
