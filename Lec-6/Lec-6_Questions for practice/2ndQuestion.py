# WAP to calculate the multiplication of two numbers

# def num_mul(a,b):
#     into = a * b
#     return into

# a = num_mul(5,6)
# print(a)



def calc_mul():
    mul=1
    for i in range(num):
        while True :
            a = int(input(f"Enter the {i+1} number :"))
            if (a == 0):
                answer = input("Are you really trying to multiply by 0? ( yes / no)")
                if answer.lower() == "yes":
                    return 0
                else :
                    print("okay lets enter the number again ! ")
                    continue
            break
        mul *= a
    return mul 
    
num = int(input("enter how many number you wanna use for multiplication : ")) 
r = calc_mul()
print("The multiplication  is : ",r)