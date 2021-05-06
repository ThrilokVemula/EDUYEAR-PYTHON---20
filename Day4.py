#Use string functions to count the occurence of 'y' in a word given by user
print("Program 1")
a = str(input("Enter a string: "))
b = 'y'
count = a.count(b)
print("The number of 'y' in the given string by user is/are: ",count)

#Take input of a string and print it's even indexed characters
print("\nProgram 2")
string = str(input("Enter a string: "))
print(string[0 : len(string) : 2])

#Create a program to swap case using string functions
print("\nProgram 3")
c = str(input("Enter a string: "))
print(c.swapcase())
