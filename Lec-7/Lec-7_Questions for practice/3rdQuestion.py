with open ("practice2.txt","w") as f :
    f.write("\nhello guys")
    f.write("\nbibek lamichhane here guys hello")
    f.write("\nlearning python")
    f.write("\nfrom apna college and wanna say hello to the apna college team")

with open("practice2.txt" , "r") as f :
    data = f.read()
new_data = data.replace("hello" , "konichiva")
print(new_data)

with open("practice2.txt" , "w") as f :
    f.write(new_data)