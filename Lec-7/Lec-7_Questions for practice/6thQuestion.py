# WAP to count the even numbers from a file containing numbers seperated by commas..( i am using list tarikale)

with open ("practice3.txt" , "r") as f :
    data = f.read()
    print(data)  # this is the output [ data = "10,23,44,51,62,71,80" ]..char instead of string

    data = data.split(",")

list = []
for idx in range(len(data)): # if we use this , python le yesari bujhxa 1 0 , 2 3 , 4 4 , 5 1 , ...reads chareacters instead of string
    list.append(int(data[idx]))
print(list)

even = 0
odd = 0
for idx in range (len(list)) :

    if (list[idx] % 2 == 0) :
        print("even!")
        even += 1

    else :
        print("Odd!")
    
        odd += 1

print("even numbers are : " , even)
print("odd numbers are : " , odd)

