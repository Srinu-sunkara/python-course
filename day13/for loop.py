'''n=int(input("enter the input: "))
res=[]
for i in range(1,n+1):
    if n%i==0:
        res.append(i)
print(f'factors of {n} = {res}')'''


'''data ={
    "sugar": 50,
    "salt" : 30,
    "cookingoil" : 70,
    "chillipowder" : 765,
    "bread" : 64,
    "butter" : 84,
    "chocolate" : 74
}
for i in data:
    print(i.ljust(20),data[i])
product = input("enter the products: ").split()
print("--------bill---------")
bill = 0
for i in product:
    print(i.ljust(20),data[i])
    bill += data[i]
print("total bill".ljust(20),bill)'''


'''s = "python programing"
d = {}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d) '''

'''s='ppppppyyyyyttt'
c=1
res=''
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        c=c+1
    else:
        res+=s[i]+str(c)
        c=1
print(res+s[i]+str(c))'''




('''pass represents empty block of code''')

'''if 10==10:
    pass

for i in range(1,10):
    pass

def verify():
    pass

class verify:
    pass'''

'''email = ''
password = ''
amount = 20000
assert amount > 0,"amount needs to be +ve"
assert email!='' and password!='','userneeds to give email and pwd'
'''






