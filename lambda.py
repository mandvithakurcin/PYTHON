>>> (lambda x: x*3)(4)
12
>>> (lambda x: x*3)([4])
[4, 4, 4]
>>> li=[1,2,3,4]
>>> l=filter(lambda x: x%2==0,li)
>>> l
<filter object at 0x0000022904249310>
>>> print(list(l))
[2, 4]
>>> l=map(lambda x: x*x,li)
>>> list(l)
[1, 4, 9, 16]
>>> l=list(map(lambda x: x+2,li))
>>> print(l)
[3, 4, 5, 6]
>>> name=["mandvi","veli","shruti","Jay"]
>>> last_name=["thakur","sethiya","tiwari","Dubey"]
>>> l=list(map(lambda x,y:x+" "+y,name,last_name))
>>> print(l)
['mandvi thakur','veli sethiya','shruti tiwari','Jay Dubey']
>>> 
