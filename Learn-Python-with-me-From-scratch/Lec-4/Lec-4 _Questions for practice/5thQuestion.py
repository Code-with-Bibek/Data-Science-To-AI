# WAP to find a way to store 9 & 9.0 as seperate value in a set...hint is we can take help of built-in-datatype

s = {9, "9.0"}
print(s)

# or

set = {
    ("float" , 9.0),
    ("int" , 9)
}
print(set)

