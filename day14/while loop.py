'''candies = 10
while candies >= 0:
    print("candies left")
    candies-=1

i = 1
while i<=10:
    print(i)
    i+=1

i = 10
while i>0:
    print(i)
    i-=1
'''

'''i = 5
while (i >= 50):
    print(i)
    i+=5'''


'''s = 'while loop'
i=0
while i<len(s):
    print(s[i])
    i+=1'''


'''l = [5467,5678,6789,987]
i  = 0
while i<len(l):
    print(l[i])
    i+=1'''

'''n = 5467
i = 0
while n>0:
    i += n%10
    n//=10
print(i)'''    


'''n = 5467
i = 0
while n>0:
    print(n%10)
    n//=10'''

'''n = 9877654433
proofdigits = 1
while n>0:
    proofdigits *= n%10
    n//=10
print("sum of digits:",proofdigits)'''


'''n = 43563
res =0
while n>0:
    rem = n%10
    res = res*10 + rem
    n//=10
print(res)'''



'''n = 123456789
res = 0
while n>0:
    rem = n%10
    res += rem
    n//=10 
print("sum of even digits:",res)'''


'''n = [12,34,7,5,0,0,5,775,0,0,4,5,7,8]
while 0 in n:
    n.remove(0)
print(n)'''

'''l = [2,3,4,5,6,7,5,44,2,5]
i = 0
j = len(l)-1
while i <= j:
    if i==j:
        print(l[i])
    else:
        print(l[i]+l[j])
    i+=1
    j-=1'''


'''data =  {"biryani":500,
         'coffe':650,
         "shawarma":330,
         "rice":369,
         'pastry':750,
        "bun":800
        }
bill = 0
while True:
    product = input("enter the product details: ")
    if product == 'E':
        print("thanks for shopping")
        print("total bill:",bill)
        break
    else:
        quantity = int(input("enter the quantity:"))
        bill += data[product]*quantity'''



