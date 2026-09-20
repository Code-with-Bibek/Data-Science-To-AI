# WAF that asks user a number ..if that number is odd , it should say " this number is odd" and " This number is even" if the number is even

def check () :
    while True:
        a = int(input("Enter a number : "))
        if(a == 0):
            print("Invalid number ! Go again...")
            continue
        elif(a %2 == 0):
            print("This number is even! ")
            break
        else:
            print("This number is odd! ")
            break

check()