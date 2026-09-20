'''
WAF to replace all the occurance of hello from q1 paragraph to konichhiva

'''
while True: 
    a = str(input("What is the name of that file ? "))
    if ( a == "practice.txt"):
            f = open("practice.txt" , "w")
            f.write("\nhello guys")
            f.write("\nbibek lamichhane here guys hello")
            f.write("\nlearning python")
            f.write("\nfrom apna college and wanna say hello to the apna college team")
            print(a.replace("hello" , "konichhiva"))
            break
    else :
                print("Try writing practice.txt")
                continue

# or we can simply use :

with open("practice1.txt" , "w") as f :
    f.write("..........")

# now we are replacing the practice.txt file which have hello to konichiva

with open ("practice.txt","w") as f :
    f.write("\nhello guys")
    f.write("\nbibek lamichhane here guys hello")
    f.write("\nlearning python")
    f.write("\nfrom apna college and wanna say hello to the apna college team")
    # data = f.read()
    # print(data)

with open("practice.txt" , "r") as f :
    data = f.read()
new_data = data.replace("hello" , "konichiva")
print(new_data)

with open("practice.txt" , "w") as f :
    print(f.write)