'''
WAP to enter marks of 3 subjects from the user and store them in a dictionary.
.start with an empty dictionary and add one by one..use subject name as key and marks as value
'''


a = int(input("Enter how many students: "))
print("_____The real game begins______")

for i in range(a):
    print(f"\nEnter marks for student {i + 1}")

    while True:
        b = int(input("Physics: "))
        if 0 <= b <= 100:
            break
        print("Invalid mark! Enter a mark between 0 and 100.")

    while True:
        c = int(input("Chemistry: "))
        if 0 <= c <= 100:
            break
        print("Invalid mark! Enter a mark between 0 and 100.")

    while True:
        d = int(input("Mathematics: "))
        if 0 <= d <= 100:
            break
        print("Invalid mark! Enter a mark between 0 and 100.")

    while True:
        e = int(input("English: "))
        if 0 <= e <= 100:
            break
        print("Invalid mark! Enter a mark between 0 and 100.")

    print("Marks recorded successfully!")

dict = {
    "physics" : b,
    "chemistry" : c,
    "maths" : d,
    "english" : e,
}
print(dict)


# or ..simply 

# a = int(input("Enter how many students: "))
# print("_____The real game begins______")

# for i in range(a):
#     print(f"\nEnter marks for student {i + 1}")

#     b = int(input("Physics: "))
#     if b > 100:
#         print("Invalid mark! Marks cannot be more than 100.")
#         continue

#     c = int(input("Chemistry: "))
#     if c > 100:
#         print("Invalid mark! Marks cannot be more than 100.")
#         continue

#     d = int(input("Mathematics: "))
#     if d > 100:
#         print("Invalid mark! Marks cannot be more than 100.")
#         continue

#     e = int(input("English: "))
#     if e > 100:
#         print("Invalid mark! Marks cannot be more than 100.")
#         continue

#     print("All marks entered successfully!")


    