# Simply means : Accessing parts of a string
#Syntax : [Starting index : ending index]

str = "learn with bibek"
print(str[0:5])
print(str[1:5])
print(str[5:10]) # here the space is also included
print(str[11:len(str)]) #why we used len()? cuz we are accessing last samma ko so , it is also equal to the total length
print(str[0:]) # if we didnt give ending index and yettikai xadiyo bhane paxi pani interpreter le bujxa ki he is trying to acess last samma ko
print(str[0:3]) # it simply mean we are trying to access from 0


print(str[0:9])