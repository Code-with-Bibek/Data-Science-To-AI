# write a recursive funcn to calculate the sum of first n natural number

# USing recursion

def calc_sum(a):
    sum = 0
    if(a<=0):
        return 0
    else:
        return a + calc_sum(a-1)


a = int(input("Enter a number :"))
b = calc_sum(a)
print(b)


# using function

def calc_sum(a):
    sum = 0
    for i in range(a+1):   # for example , the value of a is 5 --> 0 ,1 ,2 ,3 ,4
        sum += i
    return sum

a = int(input("Enter a number :"))
b = calc_sum(a)
print(b)




# (0+0) + (0+1) + (1+2) + (3+3) + (6+4) + (10+5)

