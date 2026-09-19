# WAF to find the factorial of a number n ..( n is a parameter)

def fact (a):
        result = 1
        if(a <= 0):
            return 1
        else :
            while a != 0:
                result *= a
                a -= 1
            fact(a-1)
            return result

a = int(input("Enter a number : "))
b = fact(a)
print(f"The factorial of {a} is :",b)


# or
def fact(a):
    if(a <= 0):
         return 1
    else :
         return a * fact(a-1)

a = int(input("enter a number :"))
factorial = fact(a)
print(factorial)
    
    





'''
example .. a = 5

5 * 4 * 3 * 2 * 1

'''