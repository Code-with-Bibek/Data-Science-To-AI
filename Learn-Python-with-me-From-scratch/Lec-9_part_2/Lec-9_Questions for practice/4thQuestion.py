# wap to add two complex numbers . using OOP logic

class complex:
    def __init__(self, real , img):
        self.real = real
        self.img = img

    def showNum(self):
        print(self.real,"i +" , self.img,"j")

    def __add__(self,other):
        newReal = self.real + other.real
        newImg = self.img + other.img
        return complex(newReal , newImg)
        
c1 = complex(3,4)
c1.showNum()

c2 = complex(6,7)
c2.showNum()

c3 = c1.__add__(c2)
c3.showNum()
     