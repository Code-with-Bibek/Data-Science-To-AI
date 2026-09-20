'''
if we got any sensitve data which we dont wanna print/show publically , we can print it privately but remember only inside the same class

we can make a object private by simply understanding the below program

'''

class account :
    def __init__(self, acc_number , acc_password):
        self.acc_number = acc_number
        self.acc_password = acc_password

    def acc_reset(self):
        self.acc_password

s1 = account(12345 , "bibek")  # while creating a new user , the 12345 and bibek are the details

print(s1.acc_number)
print(s1.acc_password)   # here we can use it publically . which means no security..anybody can do changes and steal your data..


# solution

class account :
    def __init__(self, acc_number , acc_password):
        self.acc_number = acc_number
        self.__acc_password = acc_password   # we use double underscore before to make acc_password private.

    def acc_reset(self):
        print(self.__acc_password)

account1 = account(12345 , "bibek")

print(account1.acc_number)

print(account1.acc_reset()) # access granted

print(account1.__acc_password)



    