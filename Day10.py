#Day10
#RECURSIVE FUNCTIONS

#Write a python program to calculate the sum of a list of numbers

print('Program 1')
def list_sum(num_list):
	if len(num_list)==1:
		return num_list[0]
	else: 	
		return num_list[0]+list_sum(num_list[1:])
      

print(list_sum([2, 4, 5, 6, 7]))

#Write a python program to solve the Fibonacci sequence using recursion

#Fibonacci series: 0 1 1 2 3 5 8 13.....

print('Program 2')
def fibonacci(n):
	if n == 1 or n == 2:
		return 1
	else:  
		return (fibonacci(n-1)+(fibonacci(n-2)))

print(fibonacci(7))	

#Write a python program to get the factorial of a non-negative number

print('Program 3')
def factorial(a):	
	if a<=1:
		return 1
	else:	
		return a*(factorial(a-1))
print(factorial(5))
