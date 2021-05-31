#Day13
#Inheritance -- acquire properties from one class and inherit to another class

#contact information
class address:
	def __init__(self,street,city):
		self.street=str(street)
		self.city=str(city)
	def show(self):
		print(self.street)
		print(self.city)

class person:
	def __init__(self,name,email):
		self.name=str(name)
		self.email=str(email)
	def show(self): 		
		print(self.name+''+self.email)

class contact(person,address):	#inheritance	
	def __init__(self,name,email,street,city):
		person.__init__(self,name,email)
		address.__init__(self,street,city)
	def show(self):		
		person.show(self)
		address.show(self)
		print()

class notebook:		
	people=dict()
	def add(self,name,email,street,city):
		self.people[name]=contact(name,email,street,city)
	def show(self,name):	
		if name in self.people:
			self.people[name].show()
		else:	
			print('Unknown',name)

notes=notebook()
notes.add('Harsh','harsh@gmail.com','Main street','Bombay')
notes.add('Amit','amit@gmail.com','Main street','Bangalore')
notes.add('Yash','yash@gmail,com','Second street','Chennai')

notes.show('Harsh')
notes.show('Ram')			