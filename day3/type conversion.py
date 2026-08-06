Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=10
>>> float(a)
10.0
>>> str(a)
'10'
>>> complex(a)
(10+0j)
>>> bool(a)
True
>>> list(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
>>> tuple(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
>>> set(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
>>> f=13.4
>>> int(f)
13
>>> str(f)
'13.4'
>>> bool(f)
True
>>> complex(f)
(13.4+0j)
>>> set(f)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    set(f)
TypeError: 'float' object is not iterable
>>> tuple(f)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    tuple(f)
TypeError: 'float' object is not iterable
dict(f)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    dict(f)
TypeError: 'float' object is not iterable
list(f)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    list(f)
TypeError: 'float' object is not iterable
c=12+3j
int(c)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
tuple(c)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
dict(c)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
s='srinivas'
a='1,23,45'
int(s,a)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    int(s,a)
TypeError: 'str' object cannot be interpreted as an integer
float(s,a)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    float(s,a)
TypeError: float expected at most 1 argument, got 2
int(a,s)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    int(a,s)
TypeError: 'str' object cannot be interpreted as an integer
tuple(s,a)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    tuple(s,a)
TypeError: tuple expected at most 1 argument, got 2
list(s,a)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    list(s,a)
TypeError: list expected at most 1 argument, got 2
list(a)
['1', ',', '2', '3', ',', '4', '5']
list(a)
['1', ',', '2', '3', ',', '4', '5']
list(s)
['s', 'r', 'i', 'n', 'i', 'v', 'a', 's']
set(s)
{'a', 'r', 'n', 'i', 's', 'v'}
set(a)
{'3', '4', '5', ',', '1', '2'}
tuple(9a)
SyntaxError: invalid decimal literal
tuple(a)
('1', ',', '2', '3', ',', '4', '5')
tuple(s)
('s', 'r', 'i', 'n', 'i', 'v', 'a', 's')
