# Write a recursive funcn to print all the elements in a list
# hint : use list and index as a parameter


def print_list(list,idx):  # or idx=0 here...--> idx = 0 is a optional parameter
    if(idx == len(list)): # Base call
        return
    print(list[idx])   # we can also print in a single line --> ,end = " "
    print_list(list,idx+1)  # we called list and plus the index

a = ["BIbek" , "Lamichhane" , "dang" , "kirtipur"]
print_list(a,idx=0)   # or idx