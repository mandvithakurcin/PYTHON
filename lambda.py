 #addtion lambda
x=(lambda a,b:a+b)(4,2)
print(x)


#multiplication lambda
x=(lambda a,b:a*b)(4,2)
print(x)


#use of lambda function
list_1 = [1,2,3,4,5]

filter( lambda x: x%2==0 , list_1 )
print( list( filter( lambda x: x%2==0 , list_1 ))


name=["mandvi","veli","shruti","Jay"]
last_name=["thakur","sethiya","tiwari","Dubey"]
l=list(map(lambda x,y:x+" "+y,name,last_name))
print(l)
['mandvi thakur','veli sethiya','shruti tiwari','Jay Dubey']

# print table 2  lambda funtions 
 table=[lambda i=x:2*i for x in range(1,11)]

for j in table:
    print(j())
