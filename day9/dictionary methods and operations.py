Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #mut ord het dynn unidu

>>> d={}
>>> d
{}
>>> type(d)
<class 'dict'>
>>> d={1:4,2:6,6:3}
>>> d
{1: 4, 2: 6, 6: 3}
>>> d{}
SyntaxError: invalid syntax
>>> d{}
>>> d={}

>>> d[1]=1
>>> d[12.3]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    d[12.3]
KeyError: 12.3
>>> d[12.3]=1
>>> d['str']
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    d['str']
KeyError: 'str'

>>> d['str']=1
>>> a[(2+3j)]=1
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a[(2+3j)]=1
NameError: name 'a' is not defined
>>> d[(2+3j)]=1
>>> d[True]=1
>>> d[[1,2,3]]=1
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    d[[1,2,3]]=1
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
>>> d[{1,2,3}]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    d[{1,2,3}]
TypeError: cannot use 'set' as a dict key (unhashable type: 'set')
d
{1: 1, 12.3: 1, 'str': 1, (2+3j): 1}
d[False]=1
d
{1: 1, 12.3: 1, 'str': 1, (2+3j): 1, False: 1}
d[1]
1
d[1]=1

d[2]=2.13
d[3]='str'
d[4]=2+3f
SyntaxError: invalid decimal literal
d[4]=2+3j
d[5]=True
d[6]=[1,2,3]
d[7]={1,2,3}
d[8]=(1,2,3)
d[9]=Frozenset({1,2,3})
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    d[9]=Frozenset({1,2,3})
NameError: name 'Frozenset' is not defined. Did you mean: 'frozenset'?
d[9]=frozenset({1,2,3})
d[10]={1:2,2:7}
d
{1: 1, 12.3: 1, 'str': 1, (2+3j): 1, False: 1, 2: 2.13, 3: 'str', 4: (2+3j), 5: True, 6: [1, 2, 3], 7: {1, 2, 3}, 8: (1, 2, 3), 9: frozenset({1, 2, 3}), 10: {1: 2, 2: 7}}
data={'name:dinesh','age:45,','course:pfs,'}
dinesh in data
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    dinesh in data
NameError: name 'dinesh' is not defined
'dinesh' in data
False
65 in data
False
'course' in data
False
data['name']
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    data['name']
TypeError: 'set' object is not subscriptable

data={'name':'dinesh','age':45,'course':'pfs'}
data['name']
'dinesh'
data.get('name')
'dinesh'
data.get('age')
45
data.get('course')
'pfs'
data.get('course','key is not present')
'pfs'
data
{'name': 'dinesh', 'age': 45, 'course': 'pfs'}
data['age']=21

data
{'name': 'dinesh', 'age': 21, 'course': 'pfs'}
data['phno']=6746567436
data
{'name': 'dinesh', 'age': 21, 'course': 'pfs', 'phno': 6746567436}
data
{'name': 'dinesh', 'age': 21, 'course': 'pfs', 'phno': 6746567436}
data.update({'email':'srinivassunkara.com','py':2026})
data
{'name': 'dinesh', 'age': 21, 'course': 'pfs', 'phno': 6746567436, 'email': 'srinivassunkara.com', 'py': 2026}
data.pop(dinesh)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    data.pop(dinesh)
NameError: name 'dinesh' is not defined
data.popitem()
('py', 2026)
data.pop('email')
'srinivassunkara.com'
data.pop('name')
'dinesh'
data id
SyntaxError: invalid syntax
id(data)
2247132631552
data.del('course')
SyntaxError: invalid syntax
del('course')
SyntaxError: cannot delete literal
del data['course']]
SyntaxError: unmatched ']'
del data['course']
data
{'age': 21, 'phno': 6746567436}
data.clear()

data
{}
data
{}



data={'name':'dinesh','age':45,'course':'pfs'}
data
{'name': 'dinesh', 'age': 45, 'course': 'pfs'}
len()
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    len()
TypeError: len() takes exactly one argument (0 given)
len(data)
3
max(data)
'name'
min(data)
'age'
data.keys()
dict_keys(['name', 'age', 'course'])
data.values()
dict_values(['dinesh', 45, 'pfs'])

data.item values()
SyntaxError: invalid syntax
data.items()
dict_items([('name', 'dinesh'), ('age', 45), ('course', 'pfs')])
sorted(data)
['age', 'course', 'name']
max(data)
'name'
min(data)
'age'

max(data)
'name'
id(data)
2247132631616
data.items()
dict_items([('name', 'dinesh'), ('age', 45), ('course', 'pfs')])
d={1:2,3:5}
m=d
m
{1: 2, 3: 5}

n
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    n
NameError: name 'n' is not defined
d
{1: 2, 3: 5}
m[3]=4
m
{1: 2, 3: 4}
m[4]=5
m
{1: 2, 3: 4, 4: 5}
n=d.copy()
n[5]=5
n
{1: 2, 3: 4, 4: 5, 5: 5}
d
{1: 2, 3: 4, 4: 5}

data
{'name': 'dinesh', 'age': 45, 'course': 'pfs'}
data.get('pfs')
data
{'name': 'dinesh', 'age': 45, 'course': 'pfs'}

data.setdefault('course','java')
'pfs'
data
{'name': 'dinesh', 'age': 45, 'course': 'pfs'}


data={'name':'dinesh','age':45,'course':'pfs'}
data.update('course':'java')
SyntaxError: invalid syntax
data.update({'course':'java'})
data
{'name': 'dinesh', 'age': 45, 'course': 'java'}

data.setdefault('batch','java')
'java'
data
{'name': 'dinesh', 'age': 45, 'course': 'java', 'batch': 'java'}
dict.fromkeys(['python','mysql','java'],0)
{'python': 0, 'mysql': 0, 'java': 0}
