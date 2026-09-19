# WAP to check if a list contains a palindrome of elements..( hint : use copy() method )
list = [2,3,2]
print(list)

if list == list.reverse():   # we cannot directly compare reverse operator ..because it just modifies the original list and after that we are comparing with none..
   print("Palindrome")       # list == none
else:
   print("NOt palindrome")


# or 

my_list = [2, 3, 2]

if my_list == my_list[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")


# or

list = [2, 3, 2]

copy_list = list.copy()
copy_list.reverse()

if list == copy_list:
    print("Palindrome")
else:
    print("Not palindrome")