

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

print(example.get("class"))  # run

print(example.get("class2"))  # none because class2 doesnot exist 