str = "i am studying python programing"
# 1 str.endswith("..")
# 2 str.capitalize("..") it capitalize the first character
# 3 str.replace(old,new) replace all occurance of old
# 4 str.find(word) returns 1st index of 1st occurrer
# 5 str.count("..") counts the occurace of substing in a string

print(str.endswith("ing")) #If we write am , then it gives false

print(str.capitalize())
print(str)  #This doesnot captalize i now
str = str.capitalize()    #Why? Because capitalize() returns a new string, but you never stored it anywhere.
                          # If you want the variable to hold the capitalized version, you must assign the returned value back:
print(str)

print(str.replace("y" , "o")) #it replaced y with o
print(str.replace("python" , "java")) #it replaced python with java

print(str.find("u"))
print(str.find("python"))
print(str.find("q")) #if we search something that doesnot exist , it gives -1 because -1 is not a valid index

print(str.count("o")) # it count how many times the o is repeated


