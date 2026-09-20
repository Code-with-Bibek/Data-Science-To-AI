'''
if hamile r+ ma file open gareu bhane , overwrite hunxa first bata...for ex:

"this is a created file"  --> if we opened this for example text.txt file in r+ and write abc ....
the result would be : abcs is a created file

'''

f = open("for r+.txt" , "w")
f.write("Testing example for r+")

f = open("for r+.txt" , "r+")
f.write("SEE!!")
print(f.read())
f.close()