# break = used to terminate a loop when encountered
# continue = terminate execution on the current iteration and continues execution of the loop with the next iteration

# i = 1
# while i <= 5 :
#     print(i)
#     if(i == 3):
#         break
#     i += 1
# print("End of loop!!")

# # Example
# num = (1,4,9,16,25,36,49,64,81,100,36,36)
# x = int(input("Enter a number :"))
# idx = 0
# while idx < len(num) :
#     if(num[idx] == x):
#         print("Found at index : " ,idx)
#         break
#     else :
#         print("The number is not here!")
        
#     idx += 1


i = 0
while i <= 5 :
   if(i == 3):
      i += 1
      continue
   print(i)
   i += 1