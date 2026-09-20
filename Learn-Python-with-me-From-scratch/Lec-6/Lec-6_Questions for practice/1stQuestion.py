# WAP to take the average of 4 numbers 


# def Calc_avg(a,b,c,d):
#     return ( a+b+c+d ) / 4
# r = Calc_avg(4,5,6,7)
# print("The average of 4 students is : ",r)

# or 

def calc_average(num):
    total = 0

    for i in range(num):
        b = int(input(f"Enter the marks of {i+1} student: "))
        total += b

    average = total / num
    return average


num = int(input("Enter how many students we are talking about: "))

average = calc_average(num)

print(f"The average of {num} students is: {average}")
