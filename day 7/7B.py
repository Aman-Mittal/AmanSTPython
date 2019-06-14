Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=(11,22)
>>> d={'name':'Prateek','Course':'MCA','College':'VIPS'}
>>> d.keys()
dict_keys(['name', 'Course', 'College'])
>>> d.values()
dict_values(['Prateek', 'MCA', 'VIPS'])
>>> d.items()
dict_items([('name', 'Prateek'), ('Course', 'MCA'), ('College', 'VIPS')])
>>> for i in d
SyntaxError: invalid syntax
>>> for i in d:
	print(i)

	
name
Course
College
>>> for i,j in d.items():print(i,'is',j)

name is Prateek
Course is MCA
College is VIPS
>>> for i in d.items():print(i)

('name', 'Prateek')
('Course', 'MCA')
('College', 'VIPS')
>>> a,b=('hello','world')
>>> a
'hello'
>>> b
'world'
>>> 
================ RESTART: C:/Users/ADMIN/Desktop/day 7/7A.py ================
<class 'dict'>
{'Name': 'Trng', 'Age': 7, 'Class': 'First'}
keys dict_keys(['Name', 'Age', 'Class'])
Values dict_values(['Trng', 7, 'First'])
items dict_items([('Name', 'Trng'), ('Age', 7), ('Class', 'First')])
dict['Name']: Trng
dict['Age']: 7
>>> d1={1:"one",2:"two"}
>>> print(d1.values())
dict_values(['one', 'two'])
>>> print(d1.keys())
dict_keys([1, 2])
>>> d1.clear()
>>> print(d1)
{}
>>> d1={1:"one",2:"two"}
>>> d2=d1.copy()
>>> print(d1)
{1: 'one', 2: 'two'}
>>> print(id(d1))
53132576
>>> print(id(d2))
53132528
>>> print(d1.get(1))
one
>>> print(d1.get(2))
two
>>> print(d1.get('one'))
None
>>> print(d1.get('one'))
None
>>> print(d1.get(22))
None
>>> print(d1.items())
dict_items([(1, 'one'), (2, 'two')])
>>> print(d1.keys())
dict_keys([1, 2])
>>> print(d1)
{1: 'one', 2: 'two'}
>>> print('After popping',d1.pop(1))
After popping one
>>> print(d1)
{2: 'two'}
>>> print(d1.pop(2))
two
>>> print(d1)
{}
>>> print('After popping  2:',d1.pop(2,100))
After popping  2: 100
>>> d1={1:"one",2:"two"}
>>> print(d1.popitem())
(2, 'two')
>>> print(d1)
{1: 'one'}
>>> d1={1:"one",2:"two"}
>>> print(d1)
{1: 'one', 2: 'two'}
>>> a=dict(one=1,two=1,three=3)
>>> d1.get(5)
>>> print(x)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    print(x)
NameError: name 'x' is not defined
>>> x=d1.get(5)
>>> print(x)
None
>>> print(d1.get(2))
two
>>> print(d1)
{1: 'one', 2: 'two'}
>>> print(d1.pop())
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    print(d1.pop())
TypeError: pop expected at least 1 arguments, got 0
>>> print(d1.pop(1))
one
>>> print(d1)
{2: 'two'}
>>> d1={1:"one",2:"two"}
>>> d1
{1: 'one', 2: 'two'}
>>> print(a)
{'one': 1, 'two': 1, 'three': 3}
>>> a=dict(one=1,two=2,three=3)
>>> a
{'one': 1, 'two': 2, 'three': 3}
>>> b={'one':1,'two':2,'three':3}
>>> b
{'one': 1, 'two': 2, 'three': 3}
>>> c=dict(zip(['one','two','three'],[10,20,30]))
>>> c
{'one': 10, 'two': 20, 'three': 30}
>>> 
>>> print(dict([('two',2),('one',1),('three',3)]))
{'two': 2, 'one': 1, 'three': 3}
>>> print(dict({'three':3,'one':1,'two':2}))
{'three': 3, 'one': 1, 'two': 2}
>>> d=dict({'three':3,'one':1,'two':2})
>>> d
{'three': 3, 'one': 1, 'two': 2}
>>> e=dict([('two',2),('one',1),('three',3)])
>>> e
{'two': 2, 'one': 1, 'three': 3}
>>> print(a==b==c==d==e)
False
>>> print(len(a))
3
>>> print(d['two'])
2
>>> a=dict(one=1,two=2,three=3)
>>> f={}
>>> print(f.fromkeys(a))
{'one': None, 'two': None, 'three': None}
>>> 
