# WAF to find in which line of the file does the word learning occur first...print -1 if the word isnt found

# with open("practice2.txt" , "r") as f :
#     # data = f.read()
#     # print(data)
#     line1 = f.readline()
#     print(line1)
#     line2 = f.readline()
#     print(line2)
#     line3 = f.readline()
#     print(line3)
#     line4 = f.readline()
#     print(line4)
#     line5 = f.readline()
#     print(line5)

#     data = f.read()
#     print(data)

#     for idx in range(len(data)):
#         if (f.readline(idx[]) == "learning"):
#             print("Learning is im 1st line!")

#         elif (f.readline(idx[]) == "learning"):
#             print("Learning is im 2nd line!")

#         elif (f.readline(idx[]) == "learning"):
#             print("Learning is im 3rd line!")

#         else :
#             print("Its in last line")

# # print(len(data))with open("practice2.txt", "r") as f:

with open("practice2.txt", "r") as f:
    line_no = 1

    for line in f:
        if "learning" in line:
            print("Learning is in line", line_no)
            break
        line_no += 1
    else:
        print(-1)

# or

with open("practice2.txt" , "r") as f :
    line_no = 1
    for line in f:
        if "learning" in line :
            print("learning is in line :" , line_no)
            line_no += 1
            break
        else :
            print(-1)



    # line1 = f.readline(1)"
    # print(line1)
    # line2 = f.readline()
    # print(line2)
    # line3 = f.readline()
    # print(line3)
    # line4 = f.readline()
    # print(line4)
    # line5 = f.readline()
    # print(line5)






