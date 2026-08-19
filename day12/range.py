#range(start,end+1,step):(0,,1)
'''for i in range(1,11):
    print(i)'''
'''for i in range(1,21,2):
    print(i)'''
'''for i in range(5,101,5):
    print(i)'''

'''for i in range(3,12,3):
    print(i)'''


'''s = (456,634,745,534,746,644)
for i in range (len(s)):
    print(i)'''

'''s = [535,543,746,736]
for i in enumerate(s):
    print(i[0],[1])'''


'''d = {1:2,2:4,3:6,4:8,5:10}
for i in enumerate(d):
    print(i[0],i[1])'''


'''for i  in range(1,11):
    if i==5:
        continue
    print(i)'''

'''for i in range(1,11):
    if i==5:
        break
    print(i)
else:
    print("End of the loop")'''


'''l = [12,13,14,15,16,18,19]
n=16
for i in l:
    if i==n:
        print(n,'found')
        break
else:
    print(n,"not found")'''

'''pin =1234
for i in range(5):
    epin = int(input("enter the pin: "))
    if epin == pin:
        print("unlock the phone")
        break
    else:
        print("invalid pin")
else:
    print("try after 30 seconds")'''

n = 18
for i in range(2,n//2+1):
    if n%i==0:
        print("not a prime number")
        break
else:
    print("prime number")







