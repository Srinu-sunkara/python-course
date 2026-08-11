Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> s='   hello   world   '
>>> s.strip()
'hello   world'

>>> s.lstrip()
'hello   world   '
>>> s.rstrip()
'   hello   world'

>>> s.replace(' ','')
'helloworld'
>>> s='python-java-flask-mysql'
>>> s.split('-')
['python', 'java', 'flask', 'mysql']
>>> s.rsplit('-')
['python', 'java', 'flask', 'mysql']
>>> s.split('$')
['python-java-flask-mysql']
>>> s.split('java')
['python-', '-flask-mysql']
>>> s
'python-java-flask-mysql'
>>> s.lsplit('-')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s.lsplit('-')
AttributeError: 'str' object has no attribute 'lsplit'. Did you mean: 'rsplit'?
>>> c='python java mysql fastapi'
>>> c='''srinivas
... ayaz
... nithin'''
>>> c
'srinivas\nayaz\nnithin'
>>> ''.join(c)
'srinivas\nayaz\nnithin'
>>> '   '.join(c)
's   r   i   n   i   v   a   s   \n   a   y   a   z   \n   n   i   t   h   i   n'
>>> '#'.join(c)
's#r#i#n#i#v#a#s#\n#a#y#a#z#\n#n#i#t#h#i#n'
>>> a='string.py'
>>> a
'string.py'
>>> a.partition('.')
('string', '.', 'py')
>>> a.lpartition('.')
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a.lpartition('.')
AttributeError: 'str' object has no attribute 'lpartition'. Did you mean: 'partition'?
a.rppartition('.')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a.rppartition('.')
AttributeError: 'str' object has no attribute 'rppartition'. Did you mean: 'rpartition'?
a.rpartition('.')
('string', '.', 'py')
a='string.py'
a.startswith('str')
True
a.endswith('py')
True
a.endswith('xl')
False
a.startwith('aayaz')
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a.startwith('aayaz')
AttributeError: 'str' object has no attribute 'startwith'. Did you mean: 'startswith'?

a.startwith('ayaz')
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a.startwith('ayaz')
AttributeError: 'str' object has no attribute 'startwith'. Did you mean: 'startswith'?
a.startswith('aayaz')
False
'python.13'.islower()
True
'python.13'.isupper()
False
'python.36'.isalpha()
False
'srinivas'.isalpha()
True
'srinivas'.isalnum()
True
'3436243878'.isalnum()
True
'  '.isspace()
True
' hello world '.isspace()
False
'      hello      world'.isspace()
False
'Hello World'.istitle()
True
'Hello World'.islower()
False
'Hello World'.isupper()
False
'HELLO WORLD'.isupper()
True
'76321645634237'.isdecimal()
True
'gugfihger'.isdigit()
False
'srinivas'.isnumeric()
False
'744'.isnumeric()
True
