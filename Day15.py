#Day15
#NumPy

#Write a NumPy program to print the NumPy version in your system

print('Program 1')
import numpy as np 
print('The version of NumPy is:\n',np.__version__)

#Write a NumPy program to convert a list of numeric value into one dimensional NumPy array

print('Program 2')
a = [12.23,13.32,100,36.32]
print('Original LIST: ',a,type(a))
b = np.array(a)
print('One dimensional Array: ',b)

#Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10

print('Program 3')
c = np.random.randint(2,11,size=(3,3))
print('3x3 matrix:\n',c)
