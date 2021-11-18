#1.Display float number with 2 decimal places using print()
float= 2.12344
format_float = "{:.2f}".format(float)
print(format_float)


#2.Take two integer numbers and  return their product.
int1=10
int2=1
def product(x,y):
return x*y
print(product(int1,int2))


# #3.Write a Python program to get the volume of a sphere with radius 10.
pi = 3.1415926535897931
r= 2
V= 4.0/3.0*pi* r**3
print('volume of sphere=: ',V)

#4.Accept two numbers from the user and multiply them together
num1=int(input("enter first no.  : "))
num2=int(input("enter second no. : "))
def prod(x,y):
  return x*y
 print(prod(num1,num2))

  
#6.Write a Python program to calculate the length of a string
string="MANDVI THAKUR"
print(len(string))

#8.Given two integer numbers return their sum. If the sum is greater than 100, then return their product.
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
 
#10.A shop will give discount of 50% if the cost of purchased quantity is more than 10000. Ask user for quantity suppose, one unit will cost 100. Judge and print total cost for user.
quantity=int(input("enter quantity of item :"))
price=quantity*100
if(price>10000):
  print("total price is :",(price/100)*50)
else:
 print("total price is :",price)   
  enter quantity of item :101
total price is : 5050.0

#9.Write a Python program to calculate the sum of three given numbers, if the values are not - equal then return four times of their sum
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

#11.To check whether a number is divisible by 8 and 12 or not.
n=int(input("enter any no. :"))
if(n%8==0 and n%12==0):
 print("{0} number is divisible".format(n))
else:
 print("{0} number is not divisible".format(n)) 

#12.To check whether a given number is even or odd.
num = int(input("Enter a number:- "))
if (num % 2) == 0:
   print("{0} is Even number".format(num))
else:
   print("{0} is Odd number".format(num))


#13	"Write a program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer. Calculate percentage and grade according to following:
Percentage >= 90% : Grade A
Percentage >= 80% : Grade B
Percentage >= 70% : Grade C
Percentage >= 60% : Grade D
Percentage >= 40% : Grade E
Percentage < 40% :  Grade F"
phy=int(input("enter physics marks :"))
chem=int(input("enter chemistry marks :")) 
bio=int(input("enter biology marks :"))
maths=int(input("enter marhematics marks :"))
comp=int(input("enter computer marks :"))
per = (phy + chem + bio + maths + comp) / 5.0
print("Percentage = ", per)
