# a) set.add(el)   used if we wanna add some elements into our set
# b) set.remove(el)   used if we wanna remove some elements from our set
# c) set.clear()      set lai empty garnalai use hunxa
# d) set.pop()       randomly elements haru bahira niskinxan print garda
# e) set.union()     combines both set values and returns new
# f) set.intersection()  combines commoon values and retutn new


set1 = {"name" , "Bachelors" , "dang" , "SMS TU" , 8}


print(set1.add("dhalpa"))
print(set1.add("dhalpa")) 
print(set1.add("chowk")) 
set1.add((1,2,4,5,7,7,9,0,10))
# set1.add([1,2,4,5,7,7,9,0,10])   #But we cannoot pass list because list ma bhako elements haru can change with time
print(set1)                # Unordered tarikale print hunxa

print(set1.remove("name"))
print(set1)

print(set1.pop())
print(set1)
print(set1.pop()) 
print(set1)
print(set1.pop())
print(set1)

set2 = {"Hello" , "Name" , "sms tu" ,8}
print(set1.union(set2))

print(set1.intersection(set2))



# print(set1.clear())
# print(set1)

