#Take variables with values of different data types
name='Ram'
age=25
salary=52050.25
Married = False
print(type(name),type(age),type(salary),type(Married))

#print these in different lines and with appropriate messages(use.format())
print("My name is", name,".I am of age", age,"years old.My salary is",salary,"rupees per month")
print("My name is"+name+".")
print("My name is {}. I am of {} years old. My salary is {} rupees.".format( name, age, salary))
print(f"My name is {name}. I am of {age} years old. My salary is {salary} rupees.")

#Practice Type conversion functions(str(),int(),etc)
x = 9
y = "100"
z = 5.25
t = True
print(type(x),type(y),type(z),type(t))

a = str(x)
b = float(x)
c = bool(x)
print(a,b,c)
print(type(a),type(b),type(c))

d = int(y)
e = float(y)
f = bool(y)
print(d,e,f)
print(type(d),type(e),type(f))

g = int(z)
h = str(z)
i = bool(z)
print(g,h,i)
print(type(g),type(h),type(i))

j = int(t)
k = str(t)
l = float(t)
print(j,k,l)
print(type(j),type(k),type(l))
