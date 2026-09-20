# WAP to find the sum of first n numbers ( using while)

sum = 0
i = 1
num = int(input("Enter a number where you wanna add upto : "))
if (num <= 0):
    print("Invalid number!!!")   
else :
    while (i <= num) :
        sum += i
        i += 1 
    print(sum)


# or

sum = 0
i = 1
while True:
    num = int(input("ENter a number you wanna add upto :"))
    if(num <= 0):
        print("Invalid number !")
    else :
        while(i <= num):
            sum += i
            i += 1
        print(sum)