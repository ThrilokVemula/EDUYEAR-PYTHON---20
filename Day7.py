#Day7
#Give all the index values of vowels

print("Program 1")
string_1 = input("Enter a string:\t")
count = 0
res = []
for i in range(len(string_1)):
    if string_1[i] in 'aeiouAEIOU' :
        print(string_1[i])
        res.append(i)
        count+=1
print("The number of vowels in the given string is:",count)
print("The vowel indices is/are:",res)

#Reverse the words of a string

print("Program 2")
string_2 = input("Enter a string:\t")
#print("The given string is:",string_2)
temp = string_2.split()
#print(temp)
temp.reverse()
string_3 = ' '.join(temp)
print("The string with reversed words is:\n",string_3)

#Remove duplicate elements without using set()

print("Program 3")
list1 = (input("Enter items into list: "))
#print(list1)
list2 = list1.split()
#print(list2)
num = [int(a) for a in list2]
print("The list with all elememts:\n",num)
list3 = []
for b in num:
    if b not in list3:
        list3.append(b)
print("The list after removing duplicate items is:",list3)
#Another method
list4 = []
[list4.append(x) for x in num if x not in list4]
print("The list after removing duplicate items:",list4)

        
       
