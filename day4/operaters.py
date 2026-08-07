Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
b=5
a+b
15
a-b
5
a*b
50
a/b
2.0
a//b
2
a**b
100000
a///b
SyntaxError: invalid syntax
2**5
32
4**2
16
3***6
SyntaxError: invalid syntax
4/2
2.0
4//2
2
a=5
b=15
a<b
True
a>b
False

a<=b
True
a==b
False
a=10
b=10
a<=b
True
a=20
a<=b
False
a=20
a=a+20
a=20
a=a+10
a
30
a=a+20
a
50
a+=10
a
60
a-=10
a
50
a-+100
-50
a-=100
A
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    A
NameError: name 'A' is not defined. Did you mean: 'a'?
a
-50
a=1000
a+=100
a
1100
a-=100
a
10003
a
1000
a*=2
a
2000
a*=12
a
24000
a/=4

a
6000.0
a//=1
a
6000.0
a//=2
a
3000.0
a//=4
a
750.0
email=true
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    email=true
NameError: name 'true' is not defined. Did you mean: 'True'?
email=true
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    email=true
NameError: name 'true' is not defined. Did you mean: 'True'?
email=True
password=False
false
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    false
NameError: name 'false' is not defined. Did you mean: 'False'?
False
False

email and password
False
login=True
login=False
display_products=True
"s" in 'aeiou'
False

''s' not 'aeiou'
SyntaxError: unterminated string literal (detected at line 1)
's'not in 'aeiou'
True
's' not  in "srinivas"
False
"s"  in 'srinivas'
True
7/2==0 and 3%2==0
False
7/2==0 and 3/6==0
False
6/2==0 and 3/6==0
False
6/2==0 and 8/2==0
False
s='python programing'
'srinu' in s
False
'srinu'not in s
True
'python' not in s
False
'programming' in s
False
'programing' in s
True

t=(10,20,30,40)
10 in t
True
'srinu' in t
False
20 not in t
False
20 in t
True
s={'name':'srinivas','no':57}
s
{'name': 'srinivas', 'no': 57}
s not in  s
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    s not in  s
TypeError: cannot use 'dict' as a dict key (unhashable type: 'dict')
name not in s
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    name not in s
NameError: name 'name' is not defined
Name not in s
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    Name not in s
NameError: name 'Name' is not defined
'name' in s
True
'name' nott in s
SyntaxError: invalid syntax
'name' not in s
False
57 in s
False
'no' in s
True
#identity ooperator
l=[1,2,3,4]
m=[1,2,3,4]
l is m
False
 l in m
 
SyntaxError: unexpected indent
l in m
False
l
[1, 2, 3, 4]
m
[1, 2, 3, 4]
l in m
False
m in l
False
n=m
#bitwise operators
11&12
8
11|12
15
11^12
7
11<<12
45056
11>>12
0
2<<2
8
2<<2
8
2<<4
32
#output operaters
a=10
b=12.3
>>> c='codegnan'
>>> print(a,b,c)
10 12.3 codegnan
>>> print('srivas')
srivas
>>> print('a=',a)
a= 10
>>> print('b='b)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print('b=',b)
b= 12.3
>>> print('c=',c)
c= codegnan
>>> print('a=',a,'b=',b,'c=',sep='\n')
a=
10
b=
12.3
c=
>>> 
... print('a=',a,'b=',b,'c=',c,sep='\n')
a=
10
b=
12.3
c=
codegnan
>>> KeyboardInterrupt
>>> 
... print('a=',a,'b=',b,'c=',sep='\t')
a=	10	b=	12.3	c=
>>> 
... print('a=',a,'b=',b,'c=',c,sep='\t')
a=	10	b=	12.3	c=	codegnan
>>> #output formating
>>> print('a=',a,'b=',b,'c=',c)
a= 10 b= 12.3 c= codegnan
>>> print(f'a={a} b={b} c={c}
...       
SyntaxError: unterminated f-string literal (detected at line 1)
>>> print(f'a={a} b={b} c={c})
...       
SyntaxError: unterminated f-string literal (detected at line 1)
>>> print(f'a={a} b={b} c={c}')
...       
a=10 b=12.3 c=codegnan
