'''
a) for loop only   syntax : for el(element) in list( or whatever) : ...
b) for loop with else    syntax : for el in list : .... else :...

'''

#example 0f (a)

Ex_list = ["Bibek" , "Laamichhane" , "kirtipur"]
for num in Ex_list :
    print(num)    # Ex_list rakhda , list nai print hunxa 6 times..


#example

tup = ("bibek Lamichhane")
for char in tup :
    print(char)



# example of (b)

tup = ("bibek Lamichhane")
for char in tup :
    print(char)
else :           # why we used else instead of just print? because it is used on some specific cases mostly with break cases
    print("end")

# examle of for..else for break

tup = ("bibek Lamichhane")
for char in tup :
    if(char == 'L') :
        print("char found!!")
        break
    print(char)
else :
    print("end")