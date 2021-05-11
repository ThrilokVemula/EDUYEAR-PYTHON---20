#Assignment on List
#Count even numbers and odd numbers

print("Program 1")
list1 = [2,5,6,37,49,24,52,14,11,9,99]
even_count = 0
odd_count = 0
for num in list1:
    if num%2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("The number of even numbers in given series is",even_count)
print("The number of odd numbers in given series is",odd_count)

#Tell max and min of the list(without using any inbuilt function like max(),min())

print("Program 2")
max = 0
min = list1[0]
for i in list1:
    if i > max:
        max = i
for j in list1:
    if j < min:
        min = j
print("The maximum value in given series is",max)
print("The minimum value in given series is",min)
#Another method
list1.sort()
print("The maximum value is",list1[len(list1)-1])
print("The minimum value is",list1[0])
        
#Check whether the whole list is palindrome or not

print("Program 3")
list3 = list(input("Enter the items into the list"))
list4 = list3[::-1]
nums = [ int(a) for a in list3]
if list4 == list3:
    print("The given list",nums,"is a palindrome")
else:
    print("The given list",nums,"is not a palindrome")
    
#print the nummbers which are palindrome inside the list

print("Program 4")
list2 = [121,222,1221,343,45654,211,344]
print(list2)
count = 0
for a in list2:
    b = a
    rev = 0
    while b>0:
        rev = rev*10 + b%10
        b = b//10
    if rev == a:
        print(a)
        count = count+1
print("The total number of palindromes are:",count)  






