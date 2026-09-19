# Dictionary in python are used to store value in key:value pair...
# hamro dictionary book bhako jastai , words haru jati pani store garera rakhna milxa but words must have their meaning and hunxan pani
# immtable(unchangeable) , unordered & duplicate value store garna mildaina in dict

# Syntax :
dict = {
    "name" : "Bibek Lamichhane" ,     # floating , list , tuple , integer , boolean , etc je ni store garna milxa
    "Roll no" : 8 , 
    "marks" : [56,45,7,89,100] ,
    "subjects" : ("Python" ,"java" ,"C"),
    "boolean" : True,
    12 : 45,   #key lai hamile je banauda ni hunxa
    56.89 : "See! we can"

}
print(type(dict) ,dict)

# if we want to print individually then ,

print(dict["name"])
print(dict["boolean"])

dict["name"] = "sudip" # we changed the name from bibek to sudip
print(dict)

dict["surname"] = "Lamichhane"
print(dict)