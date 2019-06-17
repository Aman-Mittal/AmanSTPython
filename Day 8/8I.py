Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=set("A Python Tutorial")
>>> print (x)
{' ', 'h', 'n', 'l', 'a', 't', 'u', 'r', 'T', 'A', 'o', 'i', 'y', 'P'}
>>> print(type(x))
<class 'set'>
>>> x=set(["perl","Python","Java"])
>>> print(x)
{'perl', 'Python', 'Java'}
>>> cities=set(("Paris","Lyon","London","Berlin","Paris","Birmingham"))
>>> print(cities)
{'Paris', 'Lyon', 'London', 'Birmingham', 'Berlin'}
>>> cities =set(["Frankfurt","Basel","Freilburg"])
>>> print(cities)
{'Freilburg', 'Basel', 'Frankfurt'}
>>> cities.add("Starsburg")
>>> print (cities)
{'Freilburg', 'Basel', 'Frankfurt', 'Starsburg'}
>>> cities =set(["Frankfurt","Basel","Freilburg"])
>>> cities =frozenset(["Frankfurt","Basel","Freilburg"])
>>> cities.add("Starsburg")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    cities.add("Starsburg")
AttributeError: 'frozenset' object has no attribute 'add'
>>> adjectives={"cheap","expensive","inexpensive","economical"}
>>> print(adjectives)
{'inexpensive', 'economical', 'expensive', 'cheap'}
>>> more_cities={"Delhi","Mumbai","Mandsour"}
>>> cities_backup=more_cities.copy()
>>> more_cities.clear()
>>> print(cities_backup)
{'Mumbai', 'Delhi', 'Mandsour'}
>>> x={'a','b','c','d','e'}
>>> y={'b','c'}
>>> z={'c','d'}
>>> print(x.difference(y))
{'a', 'd', 'e'}
>>> print(x.difference(y).difference(z))
{'a', 'e'}
>>> 
print(z-y)
{'d'}
>>> print(x-y)
{'a', 'd', 'e'}
>>> print(x-y-z)
{'a', 'e'}
>>> x={'a','b','c','d','e'}
>>> y={'b','c'}
>>> x.difference_update(y)
>>> print(x)
{'a', 'd', 'e'}
>>> x={'a','b','c','d','e'}
>>> y={'b','c'}
>>> x=x-y
>>> print(x)
{'a', 'd', 'e'}
>>> x={'a','b','c','d','e'}
>>> x.discard("a")
>>> print(x)
{'b', 'c', 'd', 'e'}
>>> x.discard("z")
>>> print(x)
{'b', 'c', 'd', 'e'}
>>> x={'a','b','c','d','e'}
>>> x.remove("a")
>>> print(x)
{'b', 'c', 'd', 'e'}
>>> x.remove("z")
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    x.remove("z")
KeyError: 'z'
>>> x={'a','b','c','d','e'}
>>> y={'c','d','e','f','g'}
>>> print(x.insertion(y))
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    print(x.insertion(y))
AttributeError: 'set' object has no attribute 'insertion'
>>> print(x.intersection(y))
{'c', 'd', 'e'}
>>> print(x&y)
{'c', 'd', 'e'}
>>> print(x.isdisjoint("z"))
True
>>> print(x.isdisjoint("y"))
True
>>> print(x.isdisjoint(y))
False
>>> x={'a','b','c','d','e'}
>>> y={'c','d'}
>>> prinnt(x.issubset(y))
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    prinnt(x.issubset(y))
'NameError: name 'prinnt' is not defined
>>> print(x.issubset(y))
False
>>> print(y.issubset(x))
True
>>> print(x<y)
False
>>> print(y<x)
True
>>> print(x<x)
False
>>> print(x<=x)
True
>>> x={'a','b','c','d','e'}
>>> y={'c','d'}
>>> print(x.issuperset(y))
True
>>> print(x>y)
True
>>> print(x>=y)
True
>>> print(x>=x)
True
>>> print(x>x)
False
>>> print(x.issuperset(x))
True
>>> print(x.pop())
b
>>> print(x.pop())
c
>>> y={}
>>> print(y.pop())
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    print(y.pop())
TypeError: pop expected at least 1 arguments, got 0
>>> 
