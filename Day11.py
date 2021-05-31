#Day11
#file handling and os module

#four common functions are used in python file handling
#read()
#write()
#open()
#close()

#four common modes of operation for file handling in python
#x-indicates the creation of file
#r-indicates that the file has to be read
#w-indicates to write contents in file.If file already exists,then it just overwrites the file with the current contents
#a-indicates the contents needs to be appended. File pointer will be at the end

#Creating a file
"""f = open("sample.txt","x")""" 

#Writing a file
"""f = open("sample.txt","w") 
f.write("File handling in python")
f.close()"""

#Reading a file
"""f = open("sample.txt","r") 
print(f.read())
f.close()"""

#Appending a file
"""f = open("sample.txt","a")
f.write("...Happy learning... .")
f.close()"""

#Two fie methods that are used to deal with file positions
#tell() -- To identify which position the current file pointer is located
#seek() -- To change the current file position

#tell
"""f = open("sample.txt","r")
print(f.read()) #reads the file
print(f.tell()) #The file is read thus the file pointer is now located at the end if the contents in the file
f.close()"""

#seek
"""f = open("sample.txt","r")
print(f.read())
f.seek(20)
print(f.tell())
print(f.read())
f.close()"""

"""f = open("sample.txt","r")
f.seek(5,0)
print(f.read())
f.close()"""

#The OS module can be used for file operations ad directory related operations in python
#To do these the os module needs to be imported first.

#rename() -- can be used to rename a file
#remove() -- remove or delete a file

"""import os
os.rename("sample.txt","example.txt")"""

"""import os
os.remove("example.txt")"""

#DIRECTORY OPERATIONS
#Four common directory operations in python file handling

#mkdir() -- creates a new directory
#chdir() -- changes the location of the directory
#getcwd() -- returns the current directory
#rmdir() -- removes the directory

#Creating a new directory
"""import os
os.mkdir("practice")"""

#change the location of diretory to specified path
"""import os
os.chdir("/Users/THRILOKNATH VEMULA/OneDrive/Desktop")
os.mkdir("example")"""

#Return the current working directory
"""import os
os.getcwd()"""

#Remove the specified directory
"""import os
os.rmdir("example")"""
