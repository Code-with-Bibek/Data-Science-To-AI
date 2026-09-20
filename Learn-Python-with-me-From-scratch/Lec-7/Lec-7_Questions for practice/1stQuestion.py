# WAP to create a file name "practice.txt" using python...add the following data :
'''
hello guys
bibek lamichhane here guys hello
learning python
from apna college and wanna say hello to the apna college team
'''
while True: 
    a = input("What is the name of that file ? ")
    if ( a == "practice.txt"):
            f = open("practice.txt" , "w")
            f.write("\nhello guys")
            f.write("\nbibek lamichhane here guys hello")
            f.write("\nlearning python")
            f.write("\nfrom apna college and wanna say hello to the apna college team")
            break
    else :
                print("Try writing practice.txt")
                continue




