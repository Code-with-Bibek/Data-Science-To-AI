# WAP to search for a number x in this tuple using loop..and if we find it then we will give output " Found " with the index
#   (1,4,9,16,25,36,49,64,81,100)



num = (1,4,9,16,25,36,49,64,81,100,36,36)
x = int(input("Enter a number :"))
idx = 0
while idx < len(num) :
    if(num[idx] == x):
        print("Found at index : " ,idx)
        break
    else :
        print("The number is not here!")
        
    idx += 1

