'''
Take a list of numbers:

[12, 5, 8, 21, 3, 18, 7]

Create a new list containing only numbers greater than 10.

Expected:

[12, 21, 18]

'''
list1 = []
list = [12, 5, 8, 21, 3, 18, 7]
for i in range(len(list)):
    if list[i] > 10 :
        list1.append(list[i])
print(list1)




