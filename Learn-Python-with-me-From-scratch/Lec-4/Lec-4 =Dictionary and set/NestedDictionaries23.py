# Dictionary within dictionary is a nested dictionary

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
print(example)

# if we want to print individually ;
print(example["marks"])

# or more precise and straight forward ;    dictionary bata nikalnako lagi use garne
print(example["marks"] ["mathematics"])