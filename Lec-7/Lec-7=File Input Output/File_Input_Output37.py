'''
python can be used to perform operations on a file..(read and write data)
There are two types of files : a) Text File ( .txt , .docx , .log , etc) 
                               b) binary files ( .mp4 , .mov , .png , .jpeg)

OpenRead&CloseFile --> f = open("File_name" , mode)...........mode = read(r) , write(w) , append(a)

'''
# yedi ramro kehi file chai same folder bhitra xa bhane , we only need to write the file name..and if it is in different folder , we need to give full path



print("Is python running?")
f = open("D:\Python Programming Learning\demo.txt" , "r")  # t is implicit
data = f.read()   # Hamile pahile nai read garisakim ..so , the further output for line1 & line2 will be blank
print(data , end = " ")
para1 = f.readline()
print(para1)
para2 = f.readline()
print(para2)

f.close()
'''
the few characters are:

a) r --> open for reading(default)
b) w --> open for writing...(when we use it , first all the data would be gone and paxi jeje add garxam tyo nai basxa)
c) a --> open for appending..(append at last to existing file without making a new text file
d) b --> binary mode
e) x --> create a new file and open it for reading
f) t --> text mode (default)
g) + --> opens a disk file for updating ( reading and writing)

'''
