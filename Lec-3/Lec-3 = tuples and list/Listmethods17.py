# Methods means function

# There are 5 methods .. 
# a) list.append(..)    # last ma gayera kunai value add gardinxa
# b) list.sort()     # sorts in ascending order   [1,2,3]
# c) list.sort(reverse=true) sorts in descending order   [3,2,1]
# d) list.reverse  reverses list   [3,1,2]
# e) list.insert(idx,el)   idx = kun index ma insert garne ho  & el = kun element lai add garneho
# f) list.remove   remove first occrance of the element
# g) list.pop(idx) remove element at index

list = [45,67,79,23,90]
list.append(56)  # last ma gayera 56 add gardinxa list ma
print(list)

print(list.sort())
# print(list.sort())   #it will print none because changes bhairako xa original string ma
print(list)

print(list.sort(reverse=True))

list = ["Banana" , "Apple" , "Mango"]  # we can also do sorting in strings also
print(list.sort())
print(list)

list = ['a', 'b', 'f', 't']
list.reverse()
print(list)

list.insert(2, 'g')
print(list)

list = [2,3,4,5]
list.pop(2)  # at index 2 it removes 4
print(list)





