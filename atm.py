import os
j=0
tbn=10000
atm=70000
t1=20
t2=30
t3=50
t4=50
amount=0
cust=[{"name":"sabari","pwd":"1234","bank":"Axis"},{"name":"gokul","pwd":"5678","bank":"SBI"}]

        
def adminid():
    global j
    print("Welcome to Admin portal")
    os.system('cls')
    adminname=str(input("Enter admin name: "))
    os.system('cls')
    password=input("Enter password: ")
    os.system('cls')
    l=[{"name":"sabari","pwd":"1234","bank":"Axis"},{"name":"gokul","pwd":"5678","bank":"SBI"}]
    for i in l:
        if((i['name']==adminname) and (i['pwd']==password)):
            print("Welcome to SABA BANK",adminname)
            return adminhome()
        else:
            print("Username or password not found")
            print("")
            j+=1
            if(j==3):
                print("Too many wrong attempts")
                print("")
                print("Please try after 24hrs")
            else:
                return adminid()
    


def sbal(p):
    global tbn
    print("Your balance:",tbn)
    print("Thankyou")
    logn=input("To return homepage 1 :")
    if(logn=="1"):
        print("Thank you for using ATM")
        os.system('cls')
        return customerhome()
    else:
        print("Please type 1")

def count(x):
     
    notes = [2000, 500, 200, 100]
    noteCounter = [0, 0, 0, 0]
    print ("Notes to be collected")
     
    for i, j in zip(notes, noteCounter):
        if x >= i:
            j = x // i
            x = x - j * i
            print (i ," : ", j)

             

def swithdraw(p):
    global tbn
    x = int(input("Enter Amount:"))
    os.system('cls')
    global atm
    A=("Axis")
    if (x>atm):
        print("Not enough cash in ATM")
    elif (x>tbn):
        print("Insuffient fund")
    else:
        count(x)
        y=tbn-x
        atm-=x
        
    for i in cust:
        if i['bank']==A:
            tbn=y
            print("Please collect your cash")
            print("Your balance is",tbn)
            break
        else:
            y=y-20
            tbn=y
            print("Please collect your cash")
            print("Your balance is",y)


    

    logw=input("To return homepage 1 :")
    if(logw=="1"):
        print("Thank you for using ATM")
        os.system('cls')
        return customerhome()
    else:
        print("Please type 1")

def pinchange():
    global cust
    otpsent=1234
    name= input("Enter your user name : ")
    bank=input("Enter your bank name : ")
    otp=int(input("OTP had been sent sucessfully to 73xxxxxx20 : "))
    if(otpsent==otp):
        print("New PIN(4 digit)")
        newpin=int(input())
        d=[{"name":name,"password":newpin,"bank":bank}]
        cust.append(d)
        print("PIN updated successfully")
        return customerhome()
    else:
        print("recheck")

        logp=input("To return homepage 1 :")
        if(logp=="1"):
            print("Thank you for using ATM")
            os.system('cls')
            return customerhome()
        else:
             print("Please type 1")
        
def customerhome():
    print("WELCOME")
    print("1. Money Withdrawal")
    print("2. Balance enquiry")
    print("3. Pin change")
    print("4. Exit")
    p=int(input("Enter your Choice: "))
    if(p==1):
        swithdraw(p)
    elif(p==2):
        sbal(p)
    elif(p==3):
        pinchange()
    elif(p==4):
        exithome()
    else:
        print("Invalid Input")

def adminstock():
    global atm
    global t1
    global t2
    global t3
    global t4
    atm=atm+amount
    print("Stock in ATM:",atm,"Rs")
    print("2000s:",t1)
    print("500s:",t2)
    print("200s:",t3)
    print("100s:",t4)
    logst=input("To return homepage 1 :")
    if(logst=="1"):
        print("Thank you for using ATM")
        os.system('cls')
        return adminhome()
    else:
        print("Please type 1")
          
        return adminhome()

def amtadmin():
    global atm
    global t1
    global t2
    global t3
    global t4
    amount=int(input("Enter the amount to be added:"))
    os.system('cls')
    q1=int(input("Enter the number of 2000 notes: "))
    os.system('cls')
    q2=int(input("Enter the number of 500 notes: "))
    os.system('cls')
    q3=int(input("Enter the number of 200 notes: "))
    os.system('cls')
    q4=int(input("Enter the number of 100 notes: "))
    os.system('cls')
    r=q1*2000+q2*500+q3*200+q4*100
    t1=t1+q1
    t2=t2+q2
    t3=t3+q3
    t4=t4+q4
    atm=amount+atm
    if(r==amount):
        print("Your amount",amount,"Rs updated successfully")
        print(" ")
        print("Amount updated successfully")
        print("Updation of 2000s:",q1)
        print("Updation of 500s:",q2)
        print("Updation of 200s:",q3)
        print("Updation of 100s:",q4)
        
        log=input("To logout please type 1 :")
        if(log=="1"):
            print("Thank you for using ATM")
            os.system('cls')
            return adminhome()
        else:
            print("Please type 1")
    else:
        print("Kindly check the amount")
        print("")
        loga=input("To return homepage 1 :")
        if(loga=="1"):
            print("Thank you for using ATM")
            os.system('cls')
            return adminhome()
        else:
            print("Please type 1")
          
            return adminhome()

def exitadmin():
    os.system('cls')
    return home()

def adminhome():
    print("Welcome to Admin portal")
    print("1. Amount to be updated")
    print("2. Stock in ATM")
    print("3. Exit")
    n=int(input("Enter your Choice: "))
    if(n==1):
        amtadmin()
    elif(n==2):
        adminstock()
    elif(n==3):
        exitadmin()
    else:
        print("Invalid input")

def exithome():
    return home()

def customerid(n):
    global j
    global cust
    print("Welcome to ATM")
    customername=str(input("Enter user name: "))
    os.system('cls')
    customerpassword=input("Enter Password: ")
    os.system('cls')
    
    for i in cust:
        if((i['name']==customername) and (i['pwd']==customerpassword)):
            print("Welcome to SABA BANK",customername)
            return customerhome()
        else:
            print("Username or password not found")
            print("")
            j+=1
            if(j==3):
                print("Too many wrong attempts")
                print("")
                print("Please try after 24hrs")
            else:
                return customerid(n)


def exitportal(n):
    print("Thankyou!!!")
    print(" ")
    print("Keep Banking with us")
    exit()

def home():
    print("Welcome to ATM")
    print("1. Admin page")
    print("2. Customer id")
    print("3. Exit")
    n=int(input("Enter your Choice: "))
    if(n==1):
        adminid()
    elif(n==2):
        customerid(n)
    elif(n==3):
        exitportal(n)
    else:
        print("Invalid input") 

home()