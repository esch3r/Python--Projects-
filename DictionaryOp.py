
# Dictionaries 
# Python Syntax review  12.28.18

d1 = {'a':10,'b':20,'c':30}
d2 = {'b':200,'d':400}


# Pretty much any data type can be made into a dictionary
Tupled ={(1,1):'a', (1,2):'b', (2,1): 'c', (2,2):'d'}
print(Tupled)
print(Tupled[(2,2)])
print(Tupled.popitem())
print(Tupled)

print(d1)

d1['a'] =32
d2['d']=500

print(type(d1))
print(type(d2))

print(d1)
d1.update(d2)

print(d2)
d2.update(d1)

print(d2)
print(d1.get('a'))
print(d2.items())
print(d2.keys())
print(d2.values())
print(d1.keys())
print(d2.values())
print(list(d2.items())[1][1])
