Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s='codegnan'

s
'codegnan'
type(s)
<class 'str'>

s=''
s
''
a="python'
SyntaxError: unterminated string literal (detected at line 1)
a="pytho"
b='programming'

a+b
'pythoprogramming'
a*5
'pythopythopythopythopytho'
fname='srinivas'
lname='karthik'
fname+lname
'srinivaskarthik'
a
'pytho'
b
'programming'
a*5
'pythopythopythopythopytho'
b*2
'programmingprogramming'
'*'
'*'
'*'*3090
'******************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************'
'-codegnann-'*5
'-codegnann--codegnann--codegnann--codegnann--codegnann-'
names= 'sriniva karthik suresh  ayaz lakshman'
names
'sriniva karthik suresh  ayaz lakshman'

names=[8:]
SyntaxError: invalid syntax
names=[:8]
SyntaxError: invalid syntax
names=[:7]
SyntaxError: invalid syntax
names[:7]
'sriniva'
names[8:15]
'karthik'
names[15:21]
' sures'
names[16:21]
'sures'
names[16:22]
'suresh'
s='codegnan'
s
'codegnan'
s[2]
'd'
s[5]
'n'
s='srinivas mahesh bulli'
s
'srinivas mahesh bulli'
'srinivas' in names
False
s='srinivas,mahesh,bulli'
'srinivas in names
SyntaxError: unterminated string literal (detected at line 1)
'srinivas' in names
False
's' in names
True
's' not in names
False
len(names)
37
ord('a')
97
ord('b')
98
ord('c')
99
chr(99)
'c'
chr(97)
'a'
chr(10)
'\n'
sorted(names)
[' ', ' ', ' ', ' ', ' ', 'a', 'a', 'a', 'a', 'a', 'a', 'e', 'h', 'h', 'h', 'i', 'i', 'i', 'k', 'k', 'k', 'l', 'm', 'n', 'n', 'r', 'r', 'r', 's', 's', 's', 's', 't', 'u', 'v', 'y', 'z']
max(names)
'z'
min(names)
' '
s='python programming lannguage'
s.upper()
'PYTHON PROGRAMMING LANNGUAGE'
s.lower()
'python programming lannguage'
s.tiitle()
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    s.tiitle()
AttributeError: 'str' object has no attribute 'tiitle'. Did you mean: 'title'?
s.title()
'Python Programming Lannguage'
s.swapcase()
'PYTHON PROGRAMMING LANNGUAGE'

s.foldcase()
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    s.foldcase()
AttributeError: 'str' object has no attribute 'foldcase'
s.casefold()
'python programming lannguage'
'hhvddssgcftwfcydsu'.casefold()
'hhvddssgcftwfcydsu'
s
'python programming lannguage'
s.center
<built-in method center of str object at 0x0000019B1997ACE0>
s.center(40,'.')
'......python programming lannguage......'
s.ljust(30,'#')
'python programming lannguage##'
s.rjust(100,'%')
'%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%python programming lannguage'
'12'zfill(6)
SyntaxError: invalid syntax
>>> '12'.zfill(6)
'000012'
>>> '346'.zfill(0)
'346'

>>> '346'.zfill(1)
'346'
>>> '346'.zfill(122)
'00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000346'
>>> s
'python programming lannguage'
>>> s.find(python)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    s.find(python)
NameError: name 'python' is not defined
>>> s.find('python')
0
>>> s.rfind('a')
25
>>> s.find('z')
-1
>>> s.find('a')
12
>>> s.find('c')
-1
>>> s.find('r')
8
>>> s.count('e')
1
>>> 
>>> s.count('p')
2
>>> s.index('a')
12
>>> s.index('p')
0
... 
>>> s.replace('python','java')
'java programming lannguage'
>>> s..replace('p','88')
SyntaxError: invalid syntax
s..replace('p','88')
>>> KeyboardInterrupt
>>> s.replace('p','88')
'88ython 88rogramming lannguage'
s..maketrans('aeiou','#^$%^#*')
SyntaxError: invalid syntax
s.maketrans('aeiou','#^$%^#*')
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    s.maketrans('aeiou','#^$%^#*')
ValueError: the first two maketrans arguments must have equal length
s.maketrans('aeiou','#^$*')
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    s.maketrans('aeiou','#^$*')
ValueError: the first two maketrans arguments must have equal length
s.maketrans('aeiou','#^$&*')
{97: 35, 101: 94, 105: 36, 111: 38, 117: 42}
s.translate(s.maketrans('aeiou','#^$&*'))
'pyth&n pr&gr#mm$ng l#nng*#g^'
text ='hello'
text.encode
<built-in method encode of str object at 0x0000019B1774F720>
texr.enncode()
Traceback (most recent call last):

  File "<pyshell#94>", line 1, in <module>
    texr.enncode()
NameError: name 'texr' is not defined. Did you mean: 'text'?
text.encode()
b'hello'
text.decode()
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    text.decode()
AttributeError: 'str' object has no attribute 'decode'. Did you mean: 'encode'?
b'hello'.decode()
'hello'
srinu='sardar'
srinu.encode()
b'sardar'
b'sardar'.decode()
'sardar'
