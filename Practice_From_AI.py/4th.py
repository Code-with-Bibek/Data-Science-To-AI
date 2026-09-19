'''
Take a string from the user and determine whether it is a palindrome.

Example:

madam → Palindrome
hello → Not palindrome

'''

a = (input("Enter a string :"))

is_palindrome = True

for i in range(len(a)):
    for j in range(len(a)-1,-1,-1):
        if i + j == len(a) - 1:
            if a[i] != a[j]:
                is_palindrome = False
                print(" Not palindrome")
                break
    if not is_palindrome:
        break

if is_palindrome:
    print("palindrome")
# else:
#     print("Not a palindrome")


# or simpler :


a = input("Enter a string ")
is_palindrome = True

for i in range(len(a)):

    if a[i] != a[len(a)-1-i]:
        is_palindrome = False
        break
if is_palindrome:
    print("Palindrome")
else :
    print("Not a palindrome")
    