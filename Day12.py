#Day12
#OOPS concepts

#Creating class,object and methods
#Program 1

print('Program 1')
class Employee:

	#class attribute
	company = "amazon.com"

	#constructor
	def __init__(self,name,age,salary):
		self.name =  name
		self.age = age
		self.salary = salary

	#defining methods	
	def myMethod1(self):   
		print(f"Hi {self.name}!!!")
	def myMethod2(self,city):
		print(f"{self.name}, do you live in {city}?")

#creating objects
emp1 = Employee("Harsh",34,50000)
emp2 = Employee("Amit",30,60000)

#calling methods
emp1.myMethod1()
emp1.myMethod2("Delhi")

#Program 2

print('Program 2')
class Parrot:
	
	#constructor
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	#defining methods
	def sing(self, song):
		return "{} sings {}".format(self.name, song)

	def dance(self):
		return "{} is now dancing".format(self.name)

#creating object
blu = Parrot("Blu", 10)

#calling methods
print(blu.sing("'Happy'"))
print(blu.dance())
