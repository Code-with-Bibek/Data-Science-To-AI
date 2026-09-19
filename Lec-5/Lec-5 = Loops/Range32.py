'''
Range funcn returns a sequence of numbers , starting from 0 by default..and increments by 1 ( by default) , and stop before a specific number
syntax of range : Range(start? , stop , step?) --> start & step is optional
'''
# a) for el in range(a)    --> from 0 to a number which user has given
# b) for el in range(1,a)   --> from 1 to a number "   "
# c) for el in range(1,a,3)  --> 

#Example

a = 5   # or a = range(5)
for i in range(a) :
    print(i)


#example

a = 5     # or a = range(5) 
for i in range(1,a) :
    print(i)

#Example

a = 5     # or a = range(5)    
for i in range(1,a,2) :
    print(i)
