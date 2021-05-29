#Day17
#matplotlib

import matplotlib.pyplot as plt
import numpy as np

x=np.random.randint(1,50,size=100)
y=np.random.randint(1,50,size=100)

#print(x,y)
x.sort()
y.sort()

#linegraph
plt.plot(x,y,color='blue')
plt.show()

#bargraph
plt.bar(x,y)
plt.show()

#horizontal bar graph
plt.barh(x,y,color='green')
plt.show()

#scatter graph
plt.scatter(x,y,s=10)
plt.show()

#histographs
a=np.random.randint(1,100,size=100)
b=np.random.randint(1,100,size=100)
a.sort()
b.sort()
mb=np.arange(0,110,5)
plt.hist(x,bins=mb)
plt.show()

#piecharts
activities=['Sleep','Exercise','Eat','Work','Play','others']
hours=np.random.randint(1,8,size=6)
plt.pie(hours,labels=activities,autopct='%1.1f%%')
plt.show()

#Sine and Cosine Curves
c=np.arange(0,4*np.pi,0.1)
sin=np.sin(c)
cos=np.cos(c)
plt.plot(c,sin)
plt.plot(c,cos)
#for index ,in the same order of plotting
plt.plot(c,sin,label='Sine')
plt.plot(c,cos,label='Cosine')
plt.legend()
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.show()
