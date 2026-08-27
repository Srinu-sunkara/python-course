'''def display():
    n=10
    print("inside function:",n)


display()
print("outside function:",n)'''

#local variable: variable declare inside the functioon it  acces inside the loop 
# global variable: variable declare access entire inside and outside function

'''def display():
    print("inside function:",n)

n=10
display()
print("outside function:",n)'''

'''def display():
    global n
    n=10
    print("inside the function:",n)

display()
print("outside function:",n)'''


'''def display():
    global n
    n+=10
    print("inside function:",n)

n=10
display()
print("outside function:",n)'''


'''def display():
    course="pfs"
    def update():
        nonlocal course
        course='jfs'
        print("inner function:",course)
    update()
    print("outside function:",course)
display()'''

'''l=[1,2,3,4,5]
print(sum(l))
sum = 20
print(sum)'''


'''l=[1,2,3,4,5]
print(max(l))
max = 20
print(max)'''


