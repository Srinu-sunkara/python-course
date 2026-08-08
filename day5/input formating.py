Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=input()
codegnan
a
'codegnan'
a=input("codegnan)
        
SyntaxError: unterminated string literal (detected at line 1)
a=input("codegnan)
a=input("codegnan")
        
codegnan
a=input()
        
1234
a
        
'1234'
a=input("enter  the marks")
        
enter  the marks
enter  the marks1234
        
SyntaxError: invalid syntax
enter  the marks:
1234
        
SyntaxError: invalid syntax
a=input("enter a")
        
enter a srinivas
a
        
' srinivas'
a=int(input("enter the marks")
      1234
      
SyntaxError: '(' was never closed
a=int(input("enter the marks:"))
      
enter the marks:1234
a
      
1234
b=float(input('enter the cgpa'))
      
enter the cgpa4.65
b
      
4.65
names.split()
      
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    names.split()
NameError: name 'names' is not defined
list=[srinivas]
      
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    list=[srinivas]
NameError: name 'srinivas' is not defined
list=['srinivas']
      
list
      
['srinivas']
list.split()
      
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    list.split()
AttributeError: 'list' object has no attribute 'split'
list = input("srinivas karthik")
      
srinivas karthik
list.spilt()
      
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    list.spilt()
AttributeError: 'str' object has no attribute 'spilt'. Did you mean: 'split'?
names='srinivas ayaz nithin'
      
names
      
'srinivas ayaz nithin'
names.split()
      
['srinivas', 'ayaz', 'nithin']
names='srinivas ayaz nithin 12 13 14'
      
names
      
'srinivas ayaz nithin 12 13 14'
names.split()
      
['srinivas', 'ayaz', 'nithin', '12', '13', '14']
names=set(input('enter the names'))
      
enter the names srinivas karthik
names
      
{'n', 't', 's', 'i', 'k', 'h', 'r', 'v', 'a', ' '}
names.spilt()
      
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    names.spilt()
AttributeError: 'set' object has no attribute 'spilt'
names=set(input('enter the names').split.())
      
SyntaxError: invalid syntax
names=set(input('enter the names').split())
      
enter the names srinivas karthik
enter the names srinivas karthik
      
SyntaxError: invalid syntax
names
      
{'srinivas', 'karthik'}
marks=input().split()
      
12 3 64 73 84
marks
      
['12', '3', '64', '73', '84']
map(int,marks)
      
<map object at 0x000001520852EE00>
list(map(int,marks))
      
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    list(map(int,marks))
TypeError: 'str' object is not callable
marks=list(map(int(input('enter the marks').split()))
           enter the marks
           
SyntaxError: '(' was never closed
enter the marks
           
SyntaxError: invalid syntax
marks
           
['12', '3', '64', '73', '84']
marks=list(map(int,input('enter the marks').split()))
           
enter the marks12 13 14 15 16 17
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    marks=list(map(int,input('enter the marks').split()))
TypeError: 'str' object is not callable
marks=list(map(int,input('enter the marks').split()))
           
enter the marks10 20 30
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    marks=list(map(int,input('enter the marks').split()))
TypeError: 'str' object is not callable
marks=list(map(int,input('enter the marks').split()))
           
enter the marks12344
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    marks=list(map(int,input('enter the marks').split()))
TypeError: 'str' object is not callable
marks = list(map(int,input("Enter marks: ").split()))
           
Enter marks: 12 23 45 66
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    marks = list(map(int,input("Enter marks: ").split()))
TypeError: 'str' object is not callable
marks
           
['12', '3', '64', '73', '84']
a,b=[1,2]
           
a
           
1
b
           
2
a,b,c=(1,12,13,'str')
           
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    a,b,c=(1,12,13,'str')
ValueError: too many values to unpack (expected 3, got 4)
a,b,c=(1,13,'str')
           
a
           
1
b
           
13
c
           
'str'

email,password=input('enter the email and password').split())
      
SyntaxError: unmatched ')'
email,password=input('enter the email and password').split()
      
enter the email and password srinivassunkara03@gmail.com 1234
email
      
'srinivassunkara03@gmail.com'
password
      
'1234'
a = input())
        
SyntaxError: unmatched ')'
status =eval(input())
        
2+3j
status
        
(2+3j)
(2+3j)
        
(2+3j)
type(status)
        
<class 'complex'>
status=evall(input())
        
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    status=evall(input())
NameError: name 'evall' is not defined. Did you mean: 'eval'?
status=true
        
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    status=true
NameError: name 'true' is not defined. Did you mean: 'True'?
 status=eval(input())
        
SyntaxError: unexpected indent
)
        
SyntaxError: unmatched ')'
status=evall(input())
        
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    status=evall(input())
NameError: name 'evall' is not defined. Did you mean: 'eval'?
>>> status=eval(input())
...         
status=eval(input())
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    status=eval(input())
  File "<string>", line 1
    status=eval(input())
                ^^^^^
SyntaxError: invalid syntax. Did you mean 'not'?
>>> status = eval(input())
...         
nithin
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    status = eval(input())
  File "<string>", line 1, in <module>
    __import__('idlelib.run').run.main(True)
NameError: name 'nithin' is not defined
>>> )
SyntaxError: unmatched ')'
>>> status = eval(input())
12 23 44 56
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    status = eval(input())
  File "<string>", line 1
    12 23 44 56
       ^^
SyntaxError: invalid syntax
>>> status = eval(input())
12
>>> status
12
>>> type(status)
<class 'int'>
>>> status = eval(input())
2+3j
>>> status
(2+3j)
>>> type(status)
<class 'complex'>
