# WAF to print the elements of a list in a single line..(list is a parameter)

list1 = ("Bibek")
list2 = ("Lamichhane")
print(list1 , end = " ")
print(list2)

# but i want users to write list by themselves and print the list in single line..i wanted to ask how many list you wanna write and based on that so,


a = int(input("Enter how many list you want?"))

        

def print_list(a):
    my_list = []
    for i in range(a):
        item = (input(f"enter the {i+1} list"))
        my_list.append(item)
        print(my_list)

print_list(a)

