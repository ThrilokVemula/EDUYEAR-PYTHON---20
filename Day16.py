#Pandas
#Write a Pandas program to convert a dictionary to a Pandas series

import pandas as pd 
print('Program 1')
data = {'a':100,'b':200,'c':300,'d':400,'e':800}
myvar = pd.Series(data)
print(myvar)

#Write a Pandas program to get the powers of an array values element-wise

print('Program 2')
dataset = {'X':[78,85,96,80,86],'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
var = pd.DataFrame(dataset)
print(var)

#Use any five Pandas function on a excel dataset imported as a dataframe

print('Program 3')
import numpy as np
df = pd.read_excel('D:\coalpublic2013.xlsx')
#importing the given excel data into a Pandas dataframe
print(df)

#To get the datatypes of the given excel data
print(df.dtypes)

#To get the number of rows and columns in the dataframe
print(df.shape)

#To get number of rows
print(len(df))

#print first n rows and last n rows
print(df.head(5))
print(df.tail(5))

#Append another dataframe
newdf = df.append(df)
print(newdf.shape)

#Drop duplicate rows
df = newdf.drop_duplicates()
print(df.shape)

#Get all the column names
print(df.columns)

#Pandas program to insert a column in the sixth position of excel sheet
#and fill it with NaN values
df = pd.read_excel('D:\coalpublic2013.xlsx')
df.insert(1,"column1",np.nan)
print(df)

#To read specific columns from a given excel file
cols = [1,2,4]
df = pd.read_excel('D:\coalpublic2013.xlsx',usecols=cols)
print(df)
