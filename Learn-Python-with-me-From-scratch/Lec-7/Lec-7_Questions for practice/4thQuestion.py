# WAF to find a word ( any ) from text file practice2.txt ..and print found , if it is there and not found if it isnt there

with open ("practice2.txt","w") as f :
    f.write("\nhello guys")
    f.write("\nbibek lamichhane here guys hello")
    f.write("\nlearning python")
    f.write("\nfrom apna college and wanna say hello to the apna college team")

def check_for_word():
    word = "learning"
    with open("practice2.txt" , "r") as f :
        data = f.read()
        if (data.find(word)) != -1 :
            print("Found!")
        else:
            print("NOt found")

check_for_word()
