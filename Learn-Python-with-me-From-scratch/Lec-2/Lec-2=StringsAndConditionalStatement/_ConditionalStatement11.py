# if-elif-else is a conditional statement
#for eg : if we wanna check if one is eligiable for liscense or not

age = int(input("Enter the age for inspection:"))
if age >= 18 and age < 40:
    print("You are eligiable")
elif age >= 40 and age < 50:
    print("You are eligiable")
elif age >= 50 and age < 60:
    print("You are eligiable")
elif age >= 60 and age < 70:
    print("You are eligiable but you gone old")
else:
    print("Sorry!")



