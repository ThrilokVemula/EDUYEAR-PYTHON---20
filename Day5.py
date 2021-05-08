#Assignment on For loops
#From range n to m, print all the numbers divisible by 5 and 7 both

print("Program 1")
n = int(input("\nEnter the first number of the series: "))
m = int(input("Enter the last number of series: "))
i = n
for i in range(n,m,1):
    if i%5 == 0:
        if i%7 ==0:
            print(i)
    i+=1        

#Find the sum of series 2+22+222+2222+......n terms

print("\nProgram 2")
t = int(input("\nEnter number of terms: "))
sum = 0
for i in range(1,t+1):
    k = '2'*i
    k = int(k)
    sum = sum + k
    i+=1
print("The sum of given series is :",sum)

#Assignment on While loops
#Take integer inputs from user until he/she presses q(Ask to press q to quit after every integer input). Print the sum of all numbers

print("\nProgram 3")
s = 0
while True:
    num = input("Enter a number: ")
    if num == 'q':
        break
    s = s+int(num)
print("The sum of numbers is :",s)

#Write a loop to find the factorial of the number

print("\nProgram 4")
a = int(input("Enter a number: "))
b = 1
p = 1
while b<=a:
    p = p*b
    b = b+1
print("The factorial of given number is: ",p)

#python language is best programming language

print("\nProgram 5")
st = 'python language is the best programming language'
print("The given string is:",st)
res = ''
for c in range(len(st)):
    if c%2 == 0:
        res = res + st[c].swapcase()
    else:
        res = res + st[c]
print(res)       
for d in range(len(res)):
    end_value = '-'
    if res[d] == ' ' or d == len(res)-1 or res[d+1] == ' ':
        end_value = ''
    print(res[d], end=end_value)


