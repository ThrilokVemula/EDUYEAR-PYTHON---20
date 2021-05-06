#AGE CALCULATOR
#calculate age of a person - User should enter the year of birth and the program should output the age
birthyear = int(input("Enter the year of birth :\t"))
currentyear = 2021
age = currentyear - birthyear
print("The age of the person is",age)

#SIMPLE CALCULATOR
#Get 2 numbers from user and print the result of addition, subtraction, multiplication and floor division, decimal division, remainder, power of the input numbers
a = int(input("Enter a number:\t"))
b = int(input("Enter another number:\t"))
print("The sum of given numbers is : ",(a+b))
print("The difference of given numbers is : ",(a-b))
print("The product of given numbers is :  ",(a*b))
print("The floor division of given numbers is : ",(a//b))
print("The decimal division of given numbers is : ",(a/b))
print("The remainder of the given numbers is : ",(a%b))
print("The power of the given numbers is : ",(a**b))
