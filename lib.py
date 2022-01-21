import os
j=0
l=[{"id":"100","name":"sabari","pwd":"1234",}]
br=[]
idb=1003
ida=100
idbr=100
c=[]


books = [
{"id": 1001, "Name": "Harry potter (poa)", "Arthor": "J.K Rowling", "Available": 5, "Stock":"InStock","genre":"Fantasy"},
{"id": 1002, "Name": "Tin Tin adventure", "Available": 5, "Arthor": "Herge", "Stock":"InStock","genre":"Adventure"},
{"id": 1003, "Name": "Harry potter (ps)", "Arthor": "J.K Rowling", "Available": 4, "Stock":"InStock","genre":"Fantasy"},
{"id": 1004, "Name": "Wings of fire", "Arthor": "APJ. Abdul kalam", "Available": 4, "Stock":"InStock","genre":"Autobiography"}
]

def bookidgenerator():
    global idb
    idb=idb+1
    return idb

def admidgenerator():
    global ida
    ida=ida+1
    return ida

def bridgenerator():
    global idbr
    idbr=idbr+1
    return idbr

def sort():
    search_str=input("Enter the Genre : ")
    print("Id\tName\t\t\t\t\tArthor\t\tStock\t")
    for d in books:     
        if(d['genre']==search_str):
            print(f'{d["id"]}\t{d["Name"]}\t\t\t{d["Arthor"]}\t\t{d["Stock"]}\t')
        
def cart():
    p_id=int(input("Enter the Book ID : "))
    for d in books:
        if d["id"] == p_id:
            x=d["Name"]
            print("")
            print(f'{d["id"]}\t{d["Name"]}\t\t\t{d["Arthor"]}\t\t{d["Stock"]}\t')
            print("")
    confirm = input("Do you want to take",x, "press 1... ")
    if (confirm ==1):
        c.append(d)
        return taken()
    else:
        return cart()

def taken():


            
def home():
    print("Welcome to Library")
    print("1. Admin page")
    print("2. Customer id")
    print("3. Exit")
    n=int(input("Enter your Choice: "))
    if(n==1):
        adminid()
    elif(n==2):
        customerid()
    elif(n==3):
        exitportal()
    else:
        print("Invalid input") 

def customerid():
    print("Welcome to Library")
    print("")
    print("1. View Books")
    print("2. Genre of reader")
    print("3. Previous checkout")
    print("4. Exit")
    n=int(input("Enter your Choice: "))
    if(n==1):
        display()
    elif(n==2):
        sort()
    elif(n==3):
        his()
    else:
        print("Invalid input")

def display():
    os.system('cls')
    print("")
    print("Id\tName\t\t\t\t\tArthor\t\tStock\t")
    print("")
    for d in books:
        print(f'{d["id"]}\t{d["Name"]}\t\t\t{d["Arthor"]}\t\t{d["Stock"]}\t')
    print("")

    logd=input("press 1 to go back :")
    if(logd=="1"):
        return customerid()
    else:
        print("Please type 1")
        return display()

    
def add():
    print("Welcome to Library")
    print("1. Add admin")
    print("2. Remove admin")
    print("3. Add Borrower")
    print("4. Remove Borrower")
    print("5. Exit")
    n=int(input("Enter your Choice: "))
    if(n==1):
        adda()
    elif(n==2):
        rema()
    elif(n==3):
        addbr()
    elif(n==4):
        rembr()
    elif(n==5):
        exitportal()
    else:
        print("Invalid input") 

def adminid():
    global j
    print("Welcome to Admin portal")
    os.system('cls')
    adminname=str(input("Enter your name : "))
    os.system('cls')
    password=input("Enter password : ")
    os.system('cls')
    
    for i in l:
        if((i['name']==adminname) and (i['pwd']==password)):
            print("Welcome to Library admin portal",adminname)
            return adminhome()
        else:
            print("Invalid user")
            print("")
        

def addb():
    n = int(input("Enter the no.of items need to be added : "))
    z=bookidgenerator()
    for i in range(n):
        print("Book id is",z)
        new_Name = input("Enter Book Name : ")
        new_Available = int(input("Enter Available : "))
        new_arthor=str(input("Enter Arthor name : "))
        d = [{"id": z, "Name": new_Name, "Available": new_Available, "Arthor": new_arthor}]
        os.system('cls')
        books.extend(d)
        
    logp=input("To view Display Menu press 1 :")
    if(logp=="1"):
        return bookdisplaymenu()
    else:
        print("Please type 1")

def modb():
    print("Modify the book list'n")
    print("1. Remove books")
    print("2. Customize the book's data")
    print("3. Exit")
    n=int(input("Enter your Choice: "))
    if(n==1):
        remb()
    elif(n==2):
        cusb()
    elif(n==3):
        exitportal(n)
    else:
        print("Invalid input") 

def cusb():
    os.system('cls')
    print("")
    print("Id\tName\t\t\t\t\tAvailable\t")
    print("")
    for d in books:
        print(f'{d["id"]}\t{d["Name"]}\t\t\t{d["Available"]}\t')
    print("")
    n= int(input("Enter the book id to edit"))
    for i in range(len(books)):
        if books[i]['id'] == n:
            new_name = str(input("Enter the book name : "))
            new_arthor = str(input("Enter the  arthor name : "))
            new_avail=int(input("Enter Availability : "))
            books[i]['Name'] = new_name
            books[i]['Arthor']=new_arthor
            books[i]['Available']=new_avail
            print("Data editted Successfully")
            log4=input("To return merchant page press 1 :")
            if(log4=="1"):
             return bookdisplaymenu()
            else:
                print("Please type 1")
                return adminhome()
def remb():
    n=int(input("Enter id to be removed"))
    for i in range(len(books)):
        if books[i]['id'] == n:
            del books[i]
            print(n,"'s book Removed sucessfully")
            break
    else:
        print(n,"is invalid id")

    logrp=input("To view Display Menu press 1 :")
    if(logrp=="1"):
        return bookdisplaymenu()
    else:
        print("Please type 1")
        return adminhome()

def adda():
    global l
    z=admidgenerator()
    print("Your id is",z)
    newname=input("Enter name:")
    newpass=input("Enter password:")
    d=[{'id':z,"name":newname,"pwd":newpass}]
    l+=d
    print("Admin added sucessfully")
    print(l)
    logn=input("To return adminhome press 1 :")
    if(logn=="1"):
        return home()
    else:
        print("Please type 1")
        return home()

def rema():
    r=int(input("Enter id to be removed : "))
    for i in range(len(l)):
        if l[i]['id'] == r:
            del l[i]
            print("")
            print("admin removed sucessfully : ")
            break
    else:
        print("No admin found as",r)    
    logr=input("To return adminhome press 1 :")
    if(logr=="1"):
        return adminhome()
    else:
        print("Please type 1")

def addbr():
    global br
    z=bridgenerator()
    print("Your id is",z)
    newname=input("Enter name:")
    newpass=input("Enter password:")
    d=[{'id':z,"name":newname,"pwd":newpass}]
    br+=d
    print("Borrower added sucessfully")
    print(br)
    logn=input("To return adminhome press 1 :")
    if(logn=="1"):
        return adminhome()
    else:
        print("Please type 1")
        return home()

def rembr():
    r=int(input("Enter id to be removed : "))
    for i in range(len(br)):
        if br[i]['id'] == r:
            del br[i]
            print("")
            print("Borrower removed sucessfully : ")
            break
    else:
        print("No Borrower found as",r)    
    logr=input("To return adminhome press 1 :")
    if(logr=="1"):
        return adminhome()
    else:
        print("Please type 1")

def bookdisplaymenu():
    os.system('cls')
    print("")
    print("Id\tName\t\t\t\t\tAvailable\t")
    print("")
    for d in books:
        print(f'{d["id"]}\t{d["Name"]}\t\t\t{d["Available"]}\t')
    print("")

    logd=input("press 1 to go back :")
    if(logd=="1"):
        return adminhome()
    else:
        print("Please type 1")
        return bookdisplaymenu()

def exitadmin():
    os.system('cls')
    return home()
#def out():

def adminhome():
    os.system('cls')
    print("")
    print("Welcome to Library admin portal")
    print("")
    print("1. Add Books")
    print("2. Modify Books")
    print("3. Add people")
    print("4. View Check-out cart")
    print("5. Display Books")
    print("6. Exit")
    n=int(input("Enter your Choice: "))
    if(n==1):
        addb()
    elif(n==2):
        modb()
    elif(n==3):
        add()
    elif(n==4):
        out()
    elif(n==5):
        bookdisplaymenu()
    elif(n==6):
        exitadmin()
    else:
        print("Invalid input")
home()