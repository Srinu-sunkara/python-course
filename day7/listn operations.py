Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> l=[]
>>> type(l)
<class 'list'>
>>> l=[1,2,3,5,'srinivas',True,[1,2,3],(1,2,3),1,2,3]
>>> l
[1, 2, 3, 5, 'srinivas', True, [1, 2, 3], (1, 2, 3), 1, 2, 3]

>>> a=[1,2,3]
>>> b=[4,5,6]
>>> a=b
>>> a+b
[4, 5, 6, 4, 5, 6]
>>> a*3
[4, 5, 6, 4, 5, 6, 4, 5, 6]
>>> b*2
[4, 5, 6, 4, 5, 6]
>>> a=[123,64,73,64]
>>> a
[123, 64, 73, 64]
>>> a[1]
64
>>> a[3]
64
>>> a[2]
73
>>> a
[123, 64, 73, 64]
>>> a[1:3]
[64, 73]
>>> a[1:4]
[64, 73, 64]
>>> a[0]
123
>>> a[1::2]
[64, 64]
>>> a[1::1]
[64, 73, 64]
>>> a[1:::4]
SyntaxError: invalid syntax
>>> a[1::4]
[64]
>>> a=[1,2,3,4]
>>> 1 in a
True
>>> 4in a
True
4 not in a
False
max(a)
4
min(a)
1
sorted(a)
[1, 2, 3, 4]
len(a)
4
a
[1, 2, 3, 4]
a=[275,63,63,42,97,221]
id
<built-in function id>
id()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    id()
TypeError: id() takes exactly one argument (0 given)
id(a)
2602918150656
a[0]
275
a[2]
63
a[2::3]
[63, 221]
a[-1]
221

a[-6]
275
a.insert[]
SyntaxError: invalid syntax
a.insert[2,23]
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    a.insert[2,23]
TypeError: 'builtin_function_or_method' object is not subscriptable
a.insert(2,23)
a
[275, 63, 23, 63, 42, 97, 221]
a.extend([1,2,3])
a
[275, 63, 23, 63, 42, 97, 221, 1, 2, 3]
a.extend()
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    a.extend()
TypeError: list.extend() takes exactly one argument (0 given)
a.extend([3,4])
a
[275, 63, 23, 63, 42, 97, 221, 1, 2, 3, 3, 4]
a.pop()
4
a
[275, 63, 23, 63, 42, 97, 221, 1, 2, 3, 3]
a.pop([1::3])
SyntaxError: invalid syntax
a.pop([1:3])
SyntaxError: invalid syntax
a.pop(3)
63
a
[275, 63, 23, 42, 97, 221, 1, 2, 3, 3]
a.pop(1)
63
a
[275, 23, 42, 97, 221, 1, 2, 3, 3]
a.remove(3)
a
[275, 23, 42, 97, 221, 1, 2, 3]
a.remove(42)
a
[275, 23, 97, 221, 1, 2, 3]
a.clear()
a
[]
a.pop(3::5)
SyntaxError: invalid syntax
a.pop(4)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    a.pop(4)
IndexError: pop from empty list
a=[1,2,3,4]
a.pop(1)
2
a
[1, 3, 4]

a.count()
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    a.count()
TypeError: list.count() takes exactly one argument (0 given)
a=[1,2,3,4]
a.count(2)
1
a.index(3)
2
a
[1, 2, 3, 4]
a=[1,2,3,4]
b=a
b
[1, 2, 3, 4]
b.append(3)
b
[1, 2, 3, 4, 3]
a
[1, 2, 3, 4, 3]
a=a.copy()
b.append(5)
b
[1, 2, 3, 4, 3, 5]
a
[1, 2, 3, 4, 3]

a=b.copy()
b.append(3)
a
[1, 2, 3, 4, 3, 5]
a
[1, 2, 3, 4, 3, 5]
b
[1, 2, 3, 4, 3, 5, 3]
a=[1,2,3,4]
any(a)
True
a
[1, 2, 3, 4]
a = [2,3,4]
any(a)
True
any(1)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    any(1)
TypeError: 'int' object is not iterable
a=[0,3,5,6]
any(a)
True
a=[0]
any(a)
False
all(a)
False
a=[1,2,3,4,5]
all(a)
True
all(a)
True
