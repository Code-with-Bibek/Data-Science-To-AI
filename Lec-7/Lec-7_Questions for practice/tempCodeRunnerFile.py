# WAP to count the even numbers from a file containing numbers seperated by commas

with open ("practice3.txt" , "r") as f :
    data = f.read()
    print(data)  # this is the output [ data = "10,23,44,51,62,71,80" ]..char instead of string
    data = data.split(",")

