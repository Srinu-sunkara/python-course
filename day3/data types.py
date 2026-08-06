Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#data types
#int f;oat complex
a=12
type(a)
<class 'int'>
b=13.4
type(b)
<class 'float'>
c=12+4j
type(c)
<class 'complex'>
c=12+6j
c
(12+6j)
#sequence
#str list tuple
s='codegnan'
id(s)
2704158159600

s='aaaaaaaaa'
type(s)
<class 'str'>
1=[1,2,3,4,5,6]
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
l=[1,2,3,4,5,6]
type(1)
<class 'int'>
id(l)
2704112929728
l.append
<built-in method append of list object at 0x0000027599B0CBC0>
l.append(20)
l
[1, 2, 3, 4, 5, 6, 20]
id(l)
2704112929728
type(l)
<class 'list'>
t =(1,2,3,4)
t
(1, 2, 3, 4)
id
<built-in function id>
id(t)
2704157529792
t.append(20)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    t.append(20)
AttributeError: 'tuple' object has no attribute 'append'
type (t)
<class 'tuple'>

>>> #mapping
>>> set dict
SyntaxError: invalid syntax
>>> #set dict
>>> s={1,2,3,4,)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
>>> s={1,2,3,4}
>>> s
{1, 2, 3, 4}
>>> type(s)
<class 'set'>
>>> s.append(40)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    s.append(40)
AttributeError: 'set' object has no attribute 'append'
>>> id(s)
2704157712768
>>> l
[1, 2, 3, 4, 5, 6, 20]
>>> t
(1, 2, 3, 4)
>>>  #frozen set
>>> h=({1,2,3,4,5})
>>> h
{1, 2, 3, 4, 5}
>>> type(h)
<class 'set'>
>>> id(h)
2704157712320
>>> h=frozenset({1,2,3,4)}
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
>>> h=frozenset({1,2,3,4})
>>> h
frozenset({1, 2, 3, 4})
>>> type(h)
<class 'frozenset'>
>>> h.append(30)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    h.append(30)
AttributeError: 'frozenset' object has no attribute 'append'
>>> h
frozenset({1, 2, 3, 4})
>>> id(h)
2704157713440
