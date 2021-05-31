#Day14
#Exception Handling

#Age
print('Program 1')

try:
	age=int(input('Enter the age: '))
	if age<18:
		raise ValueError
	else:	
		print("The Person is a major")

except ValueError:		
	print('The Person is a minor')

#Positive number	
print('Program 2')

try:
	num=int(input('Enter a positive integer: '))
	if num<=0:
		raise ValueError('The entered value is a negative/non-positive number')
	else:	 	
		print('The number is positive')

except ValueError as e:
		print(e)

#Zero Division Error
print('Program 3')

try:
	a=int(input('Enter a: '))
	b=int(input('Enter b: '))
	if b == 0:
		raise ZeroDivisionError
	else:	
		print('a/b = ',a/b)
except ZeroDivisionError:		
	print("The value of denominator can't be zero")