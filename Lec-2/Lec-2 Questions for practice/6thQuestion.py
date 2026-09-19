# WAP to check if a entered number is the multiple of 7 or not

num = int(input("Enter the number you wanna check :"))
if num <= 6:
    print("Error!Try another number...")
else:
    if num % 7 == 0:
        print(f"Yes the number {num} is the multiple of 7")
    else :
        print(f"No , {num} is not the multiple of 7")


# we can not only check for 7..we can do with any numbers..replacing 7 with any number 
