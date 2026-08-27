''' 
def functionname(arg):
#statements
return(optional)
'''

'''def gst(price):
    print("original price:",price)
    print('final price:',price+price*0.18)


gst(1000)
gst(40000)
gst(5000)
gst(10000)'''

'''def table(n):
    print(f'{n}-table')
    print('------------------')
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")
for i in range(1,21):
    table(i)'''

'''def isleap(year):
    if year%400==0 or (year%4==0 and year%100!=0):
        return "leap year"
    else:
        return " not a leap year"

print(isleap(2024))
print(isleap(2012))
print(isleap(2019))
print(isleap(2017))
print(isleap(2016))'''


'''def isprime(n):
    for i  in range(2,n//2+1):
        if n%i==0:
            return 'not a prime number'
    return " prime number"
print(isprime(10))'''

'''def display(name,email,pwd):
    print("name:",name)
    print("email:",email)
    print("pwd:",pwd)

display(name='dinesh',email='diinesh@gmail.com',pwd='dinesh643')
display(name='diinesh@gmail.com',email='dinesh',pwd='dinesh643')
display(name='dinesh643',email='diinesh@gmail.com',pwd='dinesh')
display(name='diinesh@gmail.com',email='diinesh@gmail.com',pwd='dinesh643')'''


'''def display(name,email,pwd=None):
    print("name:",name)
    print("email:",email)
    print("pwd:",pwd)
display('dinesh','email')
display('dinesh','email','pwd@123')
'''

'''def display(*names):# * print tuple values
    print(names)
display('dinesh')
display('dinesh','teja')
display("dinesh",'dipak','teja')'''


'''def display(**names):# ** print dictionary values
    print(names)
display(n1='dinesh')
display(n1='dinesh',n2='teja')'''