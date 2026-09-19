#Loop within a loop is nested loop

# age = int(input("Enter the age :"))
# if age >= 18:
#     if age >= 70:
#         print("You are old and cant drive ")
#     else:
#         print("you can drive and vote")
# else:
#     print("sorry ! you are not eligiable")



marks = int(input("enter your marks :"))
if marks >=40 and marks < 100:
    if marks >= 80 and marks <=90:
        print("excellent!")
    else:
        print("You are pass!")
elif marks >= 100:
    print("Marks  not typed correctly!!")
else:
    print("You are fail!!!")