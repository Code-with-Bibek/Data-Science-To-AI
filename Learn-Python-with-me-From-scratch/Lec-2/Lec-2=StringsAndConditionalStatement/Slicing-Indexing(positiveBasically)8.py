#It mean whenever a string is created in python ,all the character gets indexing internally
#simply indexing means position
#Indexing always starts from 0
# Syntax : str[..]

Inx = "Python learning" #We can give name anything... we can also use str , int , float , etc
ch = Inx[5] #This means we are accessing the string having index 5 and storing in " ch "..and that character is " n " 
print(ch)

#or

print(Inx[5]) 
print(Inx[6]) #we can also access spaces

#But we cant change the characters using index
str = "hello world"
ch = str[3] = "B"
print(ch) #We canrt manupulate