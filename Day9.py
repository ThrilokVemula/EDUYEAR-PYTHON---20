#Day 9
#Take a number from user and check whether it is prime or not. Use parameters to send the number to function.

def prime(x):
    if x > 1:
      for i in range(2,int(x/2)+1):
          if x%i == 0:
             print(x,"is not a prime number")
             break
      else:
          print(x,"is a prime number")
    else:     
        print(x,"is not a prime number")
        
a = int(input("Enter a number: "))
prime(a)


#Write a function to print n factorial.Take n value as user input and pass as parameter

def factorial(y):
    if y >= 1:
        product = 1
        for j in range(1,y+1):
            product = j*product
            j+=1
        print("The factorial of given number is :",product)    

n = int(input("Enter a number: "))
factorial(n)
    
    
        
    
