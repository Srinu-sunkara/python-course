Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> t=(1)
>>> t
1
>>> t=(1,2,,3,4)
SyntaxError: invalid syntax
>>> t=(1,2,3,4)
>>> t
(1, 2, 3, 4)
>>> t=(1,)
>>> t
(1,)
>>> t=(1,2,34,2,1)
>>> t
(1, 2, 34, 2, 1)
>>> t=(1,2,34,'str',[1,2,3,4],True)
>>> t
(1, 2, 34, 'str', [1, 2, 3, 4], True)
>>> type(t)
<class 'tuple'>
>>> id
<built-in function id>
>>> id(t)
1935849802624
>>> (1,2,3)+(1,2,3)
(1, 2, 3, 1, 2, 3)
>>> (1,2,3)*(1,2,3)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    (1,2,3)*(1,2,3)
TypeError: can't multiply sequence by non-int of type 'tuple'
>>> (1,2,3)*2
(1, 2, 3, 1, 2, 3)
>>> t=(1,2,34,5,6,5,3544)
>>> t[1]
2
>>> t[3]
5
>>> t[]
SyntaxError: invalid syntax
>>> t[0]
1
>>> t[1:5]
(2, 34, 5, 6)
>>> 2 in t
True
34 not in t
False
34 in t
True
t[-1]
3544
t=(1,234,5,65,67,77)

t5t
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    t5t
NameError: name 't5t' is not defined
t
(1, 234, 5, 65, 67, 77)
sorted(t)
[1, 5, 65, 67, 77, 234]
max(t)
234
min(t)
1
len(t)
6
t
(1, 234, 5, 65, 67, 77)
t.index[2]
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    t.index[2]
TypeError: 'builtin_function_or_method' object is not subscriptable
t.index(2)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    t.index(2)
ValueError: tuple.index(x): x not in tuple
t.index(234)
1
t.index(77)
5
sum(t)
449
all(1,5,67)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    all(1,5,67)
TypeError: all() takes exactly one argument (3 given)
all(t)
True
all((11,2,3,44))
True
a=(1,2,3,4)
a
(1, 2, 3, 4)
a=b
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    a=b
NameError: name 'b' is not defined
b=a
b
(1, 2, 3, 4)
a,b,c=a
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    a,b,c=a
ValueError: too many values to unpack (expected 3, got 4)
t=(1,2,3,4)
a,b,c=t
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    a,b,c=t
ValueError: too many values to unpack (expected 3, got 4)
a,b,c=t
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    a,b,c=t
ValueError: too many values to unpack (expected 3, got 4)
t
(1, 2, 3, 4)
a,b,c,d=t
a
1
b
2
c
3
d
4
s={1,2,3}
s
{1, 2, 3}
type(s)
<class 'set'>
s={1,2,3,4,5,6,7,7,7}
s
{1, 2, 3, 4, 5, 6, 7}
s={1,2,3,4,4,5,5,2,2}
s
{1, 2, 3, 4, 5}
s=set()
s.add(1)
s
{1}
s.add(65)
s
{65, 1}
s
{65, 1}
s.add('str')
s
{65, 1, 'str'}
s.add(23.5)
s
{65, 1, 23.5, 'str'}
a=(1,2,3,4,5)
b=(9,8,7,6,5)
5 inn a
SyntaxError: invalid syntax
5 in a
True
8 in b
True
a
(1, 2, 3, 4, 5)
a|b
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    a|b
TypeError: unsupported operand type(s) for |: 'tuple' and 'tuple'
a=(1,2,3,4)

a={1,2,3,4}
b={2,4,5,3}
a|b
{1, 2, 3, 4, 5}
a&b
{2, 3, 4}
#{1}{12}{34}
a<={4}
False
a>={4}
True
a>{2}
True
b<={3}
False
m={1,2,3,4}

b={9,8,7,6}
n.disjoint(m)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    n.disjoint(m)
NameError: name 'n' is not defined
m.isdisjoint(m)
False
m.isjoint(b)
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    m.isjoint(b)
AttributeError: 'set' object has no attribute 'isjoint'. Did you mean: 'isdisjoint'?
b.isdisjoint(m)
True
m. isdisjoint(b)
True
m. isjoint (b)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    m. isjoint (b)
AttributeError: 'set' object has no attribute 'isjoint'. Did you mean: 'isdisjoint'?
a={1,2,3,4,5}
b=a
b
{1, 2, 3, 4, 5}
b.add(23)

b
{1, 2, 3, 4, 5, 23}
a
{1, 2, 3, 4, 5, 23}
a.copy(23)
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    a.copy(23)
TypeError: set.copy() takes no arguments (1 given)
a=a.copy(23)
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    a=a.copy(23)
TypeError: set.copy() takes no arguments (1 given)
c=a.copy()
c.add(23)
a
{1, 2, 3, 4, 5, 23}
c
{1, 2, 3, 4, 5, 23}
c.add(7)
c
{1, 2, 3, 4, 5, 7, 23}
a
{1, 2, 3, 4, 5, 23}
a.pop()
1
a.pop()
2

a.remove(2)
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    a.remove(2)
KeyError: 2
a.remove(3)
a
{4, 5, 23}
a.discard(5)
a
{4, 23}
a.discard(4,23)
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    a.discard(4,23)
TypeError: set.discard() takes exactly one argument (2 given)
a.clear
<built-in method clear of set object at 0x000001C2B9A62B20>
a.clear()
a
set()
a=frozenset({1,2,4,5})
a
frozenset({1, 2, 4, 5})

a.add(2)
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    a.add(2)
AttributeError: 'frozenset' object has no attribute 'add'
