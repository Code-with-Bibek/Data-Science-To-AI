

class person :
    name = "anonymous"

    def Hello(self):
        print("Hello person!")

    def Welcome(self):
        pass  # we get access by calling the funcn in another funcn

p1 = person()
# print(p1.Welcome())  # we cannot print and access "Hello person!" outside the class
print(p1.name) 
print(p1.Hello())