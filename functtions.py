#area of triangle 
def area (a,b,c):
    s=(a+b+c)/2
    areaoftriangle=math.sqrt(s*(s-a)*(s-b)*s-c)
    print("area triangle=",areaoftriangle)
area(1,6,9)

#pass list as argument 
def list(li):
    for i in li:
        print(i)

list1=[1,2,3,4,7,5,6]
list(list1)

#function with arguments
def fact(n):
    if(n%2==0):
        print ("even")
    else:
        print ("odd")


# local and global variable
x = "good" 
def myfunc():
  x = "vgood" 
  print("x  local ".format(x))

myfunc()
print("x global ".format(x))

x = "mandvi"
def myfunc():
    global x   
    x = "mandvi thakur" 
    print("x local ".format(x))

myfunc()
print("x  global ".format(x))

int1=10
int2=1
def product(x,y):
  return x*y
print(product(int1,int2))
#output-10


# Accept two numbers from the user and multiply them together
num1=int(input("enter first no.  : "))
num2=int(input("enter second no. : "))
def prod(x,y):
  return x*y
print(prod(num1,num2))
# enter first no.  : 2
# enter second no. : 2
# 4

# Given two integer numbers return their sum. If the sum is greater than 100, then return their product.
num1=50
num2=51
def prod(x,y):
  return x*y
def sum(x,y):
  return x+y
sum=sum(num1,num2)
if(sum>100):
  print("product :",prod(num1,num2))
else:
  print("sum=",sum)
#product:2550


# Write a Python program to calculate the sum of three given numbers, if the values are not - equal then return four times of their sum
num1=4
num2=4
num3=2
def sum(num1,num2,num3):
  return num1+num2+num3
sum=sum(num1,num2,num3)
if(num1==num2 and num1==num3):
  print("sum :",sum)
else:
  print("sum :",sum*4)
#sum:40

# find digital sum of a given Number
#    ex: n=111  Digital sum----->1+1+1=3
def getsum(n):
  sum=0
  num = str(n)
  for i in num:
    sum = sum + int(i)
  return sum

n=int(input("Enter the number:"))
print(getsum(n))
# Enter the number:111
# 3

# Program to check whether a given number is a palindrome or not

def reverseDigits(num) :
	rev_num = 0;
	while (num > 0) :
		rev_num = rev_num * 10 + num % 10
		num = num // 10	
	return rev_num

def isPalindrome(n) :
	rev_n = reverseDigits(n);
	if (rev_n == n) :
		return 1
	else :
		return 0
  n = 111	
if isPalindrome(n) == 1 :
  print("Is", n, "a Palindrome number? ->", True)

else :
  print("Is", n, "a Palindrome number? ->", False) 

# find the digital product of a given number
#    ex: n=12   Digital product ----->1*2=2
def getProduct(n):
  product = 1
  num = str(n)
  for i in num:
    product = product * int(i)
  return product

n=int(input("Enter the number:"))
print(getProduct(n))
# Enter the number:12
# 2



