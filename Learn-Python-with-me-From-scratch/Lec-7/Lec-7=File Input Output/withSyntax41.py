with open("sample.txt" , "r") as f :    # as means alias...means same thing for opening of file
    data = f.read()
    print(data)
f.close()   # not necessary to use close here\

# yesle " open("sample.txt" , "r") " return gareko value lai hamile youta alias diyeko xam...name deko rako xam


with open("sample.txt" , "w") as f : 
    f.write("It is using with syntax")
