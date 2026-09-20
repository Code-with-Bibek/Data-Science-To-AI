'''
when a function calls itself repeatedly...

fun fact : if any work is done using loop , then that same work can be done using recursion and vice versa

imp note : Base case/call hunai parxa

'''

def recursion(n):
    if(n == 0 or n == 1):  # base call
        return 1
    print(n)
    recursion(n - 1)
    print("END")

print(recursion(0))


# using recursion for factorial       ( n! = (n - 1)! * n ) --> Here n! is a big value and it depend on its own smaller value (n-1)! --> we call this " Recurrence Relation"
# Recurrence relation --> which is reoccuring , recurrent , which is repeating

# def recursion(n):
#     if(n == 0 or n == 1):  # base case
#         return 1
#     else:
#         return n * recursion(n - 1)

# n = int(input("enter a number :"))
# a = recursion(n)
# print(a)