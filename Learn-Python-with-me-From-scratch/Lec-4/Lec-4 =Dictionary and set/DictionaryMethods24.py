# My_dict is just an dictionary name .. we can use any names for dictionary

# a) My_dict.keys()    --> returns all keys of that dictionary
# b) My_dict.values()   --> retrns all values of that dictionary
# c) My_dict.items()   --> returns all (key , value) pairs in an tuple
# d) My_dict.get("key")     --> return the key according to value
# e) My_dict.update({new_dict})  --> returns especified items to the dictionary

example = {
    "name" : "Bibek Lamichhane",
    "class" : "Bachelors",
    "roll_no" : "8",
    "subjects" : ["Calculus" , "statistics" , "python" , "linear algebra"],
    "marks" : {
        "physics" : 53,
        "chem" : 67,
        "mathematics" : 12,
    }
}
print(example.keys())
print(example.values())

print(list("example"))   # if hamilai diyeko dict chai list or tuple ma convert garnu pareko aawastha ma 
print(len(list("example")))   #if length kati ho bhanera bujhda

print(example.items())   #tuple ko form ma display hunxa

print(example.get("marks"))    # youta single key:value lai display garne bela , yo use garinxa

# If malai specific pair lai access garnu xa tuple ko form ma then , we will use ;
pairs = list(example.items())
print(pairs[3])


example.update({"city" : "Kathmandu" })
print(example)