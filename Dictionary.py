my_dict={1:"mandvi",2:"thakur"}
print(my_dict)
{1: 'mandvi', 2: 'thakur'}

my_dict={"fist_name":"mandvi","last_name":"thakur","hobby":["painting","sketching"]}
print(my_dict["hobby"])
['painting','sketching']

my_dict=dict({1:"mandvi",2:"thakur"})
print(my_dict)
{1: 'mandvi', 2: 'thakur'}

my_dict=dict([(1,"mandvi"),(2,"thakur")])
print(my_dict)
{1: 'mandvi', 2: 'thakur'}

my_dict=dict([(1,"mandvi"),(2,"thakur")])
my_dict["age"]=20
print(my_dict)
{1: 'mandvi', 2: 'thakur', 'age': 20}

my_dict={1:"mandvi",2:"thakur",5:"name"}
print(my_dict.pop(5))
print(my_dict)
print(len(my_dict))
name
{1: 'mandvi', 2: 'thakur'}
2

x = my_dict.values()
print(x)
y= my_dict.keys()
print(y)
dict_values(['mandvi', 'thakur', 'C1', 33])
dict_keys([1, 2, 'Field', 'age'])
x= my_dict.get(1)
print (x)
x= my_dict.keys()
print (x)
my_dict["Field"]="CI"
my_dict["age"]=33
print (x)
print(my_dict)
mandvi

y_dict={1:"mandvi",2:"thakur",5:"name"}
for i in my_dict.keys():
  print(i)
1
2
5
my_dict={1:"mandvi",2:"thakur",5:"name"}
for i in my_dict.keys():
  print(i ," : ",my_dict[i])
1  :  mandvi
2  :  thakur
5  :  name
my_dict={1:"mandvi",2:"thakur",5:"name"}
for x, y in my_dict.items():
  print(x," : ", y)
1  :  mandvi
2  :  thakur
5  :  name

  myDict = {x: x**2 for x in [1,2,3,4,5]}
print (myDict)
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
li=[1,2,3,4,5]

myDict = {x: x**3 for x in li}
print (myDict)
{1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
