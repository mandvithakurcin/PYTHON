#empty tuple 
tuple=()
print(tuple)

#tuple
tuple=(1,2,3,4,5)
print(tuple)

#mixed data type 
tuple=(1,2,3),"mandvi",(5,6,7)
print(tuple)

#indexing in tuple
tuple=(1,2,3),"mandvi",(5,6,7),[6,8,9]
print(tuple[0])
print(tuple[3])

#tuple unpacking 
tuple=33,'CSIT',2021
print(tuple)
a,b,c=tuple
print(a)
print(b)
print(c)

#slicing
tuple=(1,2,3,4,5)
print(tuple[-2:-2])
# elements beginning to end
print(tuple[:])

#max, min , length
tuple = (1,2,3,4,5)
maximum = max(tuple)
minimum = min(tuple)

print("Max: ", maximum)
print("Min: ",minimum)
print("Len: ", len(tuple))

#deleting a tuple
tuple = (22,33,44,55,66,77)

print(tuple)
del tuple

thistuple=('m','a','n','d','v','i')
print(thistuple)
print(thistuple.count('A'))
print(thistuple.count('y'))
print(thistuple.index('A'))
print('a' in thistuple)
print('z' in thistuple)
for m in ('mandvi','priya'):
    print('hello',m)
a=(6,8,9)
for n in a:
    print(2*n)
b=[5,9,4]
b.sort()
print(b)
b=sorted(a)
a=(6,3,7)
b=sorted(a)
print(b)
print(a)
