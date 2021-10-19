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
  print("x with value {0} is local here ".format(x))

myfunc()
print("x with value {0} is global ".format(x))

x = "mandvi"
def myfunc():
    global x   
    x = "mandvi thakur" 
    print("x global ".format(x))

myfunc()
print("x with value {0} is global ".format(x))
