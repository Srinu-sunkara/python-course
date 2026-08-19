'''fa = eval(input('Follows the Account: '))
if fa:
    cf = eval(input('Close Friends: '))
    if cf:
        print("Story Visible")
    else:
        print("Not in Close Friends list")
else:
    print("Follow The Account First")'''



'''reg = eval(input("regestered: "))
if reg:
    fee = eval(input("fee paid"))
    if fee:
        print("tournament entry confirmed")
    else:
        print("entry fee pending")
else:
    print("regestration required")'''



data = {
    'srinivas':{'status':True,'python':90,'my sql':95,'flask':98},
    'nithin':{'status':True,'python':94,'my sql':67,'flask' :79},
    'ayaz':{'status':False,'python':4,'my sql':6,'flask':8},
    'karthik':{'status':True,'python':76,'my sql':64,'flask':78},
    'ram prasad':{'status':True,'python':84,'my sql':79,'flask':85}
}
name = input('enter the name: ')
if name in data:
    if data[name]['status']:
        sum =data[name]['python']+data[name]['my sql']+data[name]['flask']
        avg = sum/3
        print(f"hello {name},,")
        print(f'your average score is {avg}')
        if avg >= 90:
            print("outstanding")
        elif avg >= 80:
            print("very good")
        elif avg >= 70:
            print("good")
        elif avg >= 60:
            print("average")
        elif avg >= 40:
            print("bad")
        else:
            print("failed")
    else:
        print(f"{name} did not attended the exam")
else:
    print(f"{name} not found in data")                    
            



    


