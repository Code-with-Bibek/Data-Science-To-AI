'''
if we used w+ then hamro text file truncate hunxa...means change hunca , completely wiped out hunca..
and then we can write

'''

# f = open("for w+.txt" , "r")
f = open("for w+.txt" , "w+")
# f.write("SEE!!")
   # pointer aaba SEE!! ko last ma xa so, read garxa yesto : ng example for r+
print(f.read())
f.write("See!!")
f.close()