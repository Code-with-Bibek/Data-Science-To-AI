# WAP to count how many times the given alphabets are repeated ..("e","f","g","e","f","g","a","e","e")

tupl = ("e","f","g","e","f","g","a","e","e")
print(tupl.count("e"))
print(sorted(tupl))
print(tuple(sorted(tupl)))

# or if i wanted to count every elements then ,

tupl = ("e","f","g","e","f","g","a","e","e")
for i in set(tupl):
    print(i , "=" , tupl.count(i))  



# Working principle of just above code-->

# list contains all the alphabets:

# ["e", "f", "g", "e", "f", "g", "a", "e", "e"]
# set(list) is used to remove duplicate values from the list.

# After applying set(), the list becomes a collection of unique alphabets:

# {'e', 'f', 'g', 'a'}

# The for loop takes each unique alphabet one by one:

# for i in set(list):
# i stores the current alphabet during each loop.
# list.count(i) counts how many times that alphabet appears in the original list.

# Example:

# list.count("e")

# counts the number of times "e" appears and returns:

# 4

# The print() statement displays the alphabet and its count:

# print(i, "=", list.count(i))