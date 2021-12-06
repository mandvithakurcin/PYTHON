 #addtion lambda
x=(lambda a,b:a+b)(4,2)
print(x)


#multiplication lambda
x=(lambda a,b:a*b)(4,2)
print(x)


#use of lambda function
list_1 = [1,2,3,4,5]

filter( lambda x: x**2==0 , list_1 )
print( list( filter( lambda x: x**2==0 , list_1 )))

#list lambda
name=["mandvi","veli","shruti","Jay"]
last_name=["thakur","sethiya","tiwari","Dubey"]
l=list(map(lambda x,y:x+" "+y,name,last_name))
print(l)


# print table 2  lambda funtions 
 table=[lambda i=x:2*i for x in range(1,11)]

for j in table:
    print(j())
  
# list 
list1 = [1, 3, 5, 7, 9]
list2 = list(map(lambda x: x * 2 , list1))
print(list2)

#adding list
list1=[2,3,4,5,6]
list2=[4,5,6,7,8]
print(list(map (lambda x,y:x+y,list1,list2)))

max=reduce (lambda x,y: x if x>y else y,list1)
print(max)
print("mandvi".upper())

def func1(x):
  return x+5

print(func1(5))

print(list(map(lambda x:pow(x,3), list1)))

str1= ['hii', 'hello']
print(list(map(lambda x: x.upper(), str1)))

age=[5,6,7,8,9,10,11]
print(list(filter(lambda x: x<10, age)))

mylist = map(lambda x : x*2, [x for x in range(1,11)])
print(list(mylist))
