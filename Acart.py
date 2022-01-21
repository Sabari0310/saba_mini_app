import os
id=100
idu=1
admin=[{'name':'sabari','password':'1234'}]
merch=[{'id':100,'name':'kd','password':'1234'}]
merchapp=[]
user=[]
order=[]
kart=[]
order_number=4567
temp=[]
count=0

shopping = [
{"id": 1001, "Name": "HP", "Available": 100, "Original_Price": 24000,"Offer%": 20,"Price": 25000},
{"id": 1002, "Name": "DELL", "Available": 100, "Original_Price": 34000, "Offer%": 11, "Price": 35000},
{"id": 1003, "Name": "ASUS", "Available": 100,  "Original_Price": 27000, "Offer%": 15,"Price": 28000},
{"id": 1004, "Name": "APPLE", "Available": 100,  "Original_Price": 59000, "Offer%": 23,"Price": 60000},
{"id": 1005, "Name": "ACER", "Available": 100,  "Original_Price": 23000, "Offer%": 25,"Price": 24000},
{"id": 1006, "Name": "SAMSUNG", "Available": 100,  "Original_Price": 34000, "Offer%": 50,"Price": 35000},
{"id": 1007, "Name": "OPPO", "Available": 100,  "Original_Price": 14000, "Offer%": 5,"Price": 15000},
{"id": 1008, "Name": "XAOMI", "Available": 100,  "Original_Price": 44000, "Offer%": 2,"Price": 45000},
{"id": 1009, "Name": "HUAWEI", "Available": 100,  "Original_Price": 19000, "Offer%": 25,"Price": 20000},
{"id": 1010, "Name": "VIVO", "Available": 100,  "Original_Price": 11000, "Offer%": 10,"Price": 12000}
]

def adminlogin():
    global admin
    global count
    os.system('cls')
    print("Welcome to A-cart's Admin portal!")
    print("")
    aname=input("Enter adminname:")
    apassword=input("Enter password:")
    print("")
    for i in admin:
        if((i['name']==aname) and (i['password']==apassword)):
            a=i
            os.system('cls')
            return adminhome()
        else:
            print("Invalid input: ")
            count+=1
        if(count==3):
            print("")
            print("Too many wrong attempts")
            print("")
        else:
            return home()

def appm():
    global merchapp
    if(len(merchapp)==0):
        print("No merchant to be approved")
    else:
        for i in merchapp:
            print(i)
            adminapp=input("Approve(A)/Not Approve(N):")
            if(adminapp=='A'):
                merch.append(i)
        merchapp=[]
        print("")
        print("Approved sucessfully")
    logap=input("To return adminhome press 1 :")
    if(logap=="1"):
        return adminhome()
        
    else:
        print("Please type 1")

def lom():
    a=(merch.get("id"))
    b=(merch.get("name"))
    print("ID = ",a)
    print("Name = ",b)
    

def addm():
    global merch
    z=idgenerator()
    print("Your id is",z)
    newname=input("Enter name:")
    newpass=input("Enter password:")
    d=[{'id':z,"name":newname,"password":newpass}]
    merch+=d
    print("Merchant added sucessfully")
    print(merch)
    logn=input("To return adminhome press 1 :")
    if(logn=="1"):
        return adminhome()
    else:
        print("Please type 1")
    
def remm():
    r=int(input("Enter id to be removed : "))
    for i in range(len(merch)):
        if merch[i]['id'] == r:
            del merch[i]
            print("")
            print("Merchant removed sucessfully : ")
            break
    else:
        print("No Merchant found as",r)    
    logr=input("To return adminhome press 1 :")
    if(logr=="1"):
        return adminhome()
    else:
        print("Please type 1")

def merl():
    global count
    os.system('cls')
    print(admin)
    print("Welcome to A-cart's Merchant portal!")
    print("")
    mname=input("Enter name:")
    mpassword=input("Enter password:")
    print("")
    for i in merch:
        if((i['name']==mname) and (i['password']==mpassword)):
            a=i
            return merchlogin()
        else:
            print("Invalid input: ")
        for i in merchapp:
            if((i['name']==mname) and (i['password']==mpassword)):
                a=i
                print("Waiting for approval")
                print("")
                print("Please try later")
                logr=input("To return adminhome press 1 :")
                if(logr=="1"):
                    return mlogin()
            else:
                print("Please type 1")
                
        count+=1
        if(count==3):
            print("")
            print("Too many wrong attempts")
            print("")
        else:
            return home()

def mers():
    global merchapp
    z=idgenerator()
    print("Your id is",z)
    nname=input("Enter name:")
    npass=input("Enter password:")
    print("Waiting for approval...")
    y={'id':z,"name":nname,"password":npass}
    merchapp.append(y)
    logm=input("To return Merchant home press 1 :")
    if(logm=="1"):
        return mlogin()
    
    else:
        print("Please type 1")

def merchlogin():
    os.system('cls')
    print("Welcome to A-cart's merchant login page")
    print("")
    print("1. Add product")
    print("2. Remove product")
    print("3. Display menu")
    print("4. Total products available")
    print("5. Total income")
    print("6. Admin Home")

    n=int(input("Enter your choice:"))
    if(n==1):
        addp()
    elif(n==2):
        rem()
    elif(n==3):
        admindisplaymenu()
    elif(n==4):
        tpa()
    elif(n==5):
        toti()
    elif(n==6):
        exitadminhome()
    else:
        print("Invalid input")
        return home()

def addp():
    n = int(input("Enter the no.of items need to be added : "))
    for i in range(n):
        new_id = int(input("Enter id : "))
        new_Name = input("Enter Name : ")
        new_Available = int(input("Enter Available : "))
        offer = int(input("Enter Discount : "))
        new_original = int(input("Enter the original price : "))
        new_Price=int((offer/100)*new_original)
        d = [{"id": new_id, "Name": new_Name, "Available": new_Available, "Original_Price": new_original, "Offer%": offer, "Price": new_Price}]
        os.system('cls')
        shopping.extend(d)
        
    logp=input("To view Display Menu press 1 :")
    if(logp=="1"):
        return admindisplaymenu()
    else:
        print("Please type 1")

def rema():
    productId = int(input("Enter the id need to be deleted : "))
    found = False
    for d in shopping:
        found = d["id"] == productId
        if found != True:
            temp.append(d)
            continue
        if found == True:
            n=int(input("Enter number of products needed to be removed : "))
            print("")
            d["Available"] -= n
    print("Deleting item....")
    if len(temp) == d:
        print("")
        print(f"{productId} not found")
    else:
        print("")
        print(f"{productId}'s one available is removed from the list")
    admindisplaymenu()

    loge=input("To view Display Menu press 1 :")
    if(loge=="1"):
        return admindisplaymenu()
    else:
        print("Please type 1")

def remp():
    n=int(input("Enter id to be removed"))
    for i in range(len(shopping)):
        if shopping[i]['id'] == n:
            del shopping[i]
            print(n,"'s Product Removed sucessfully")
            break
    else:
        print(n,"is invalid id")

    logrp=input("To view Display Menu press 1 :")
    if(logrp=="1"):
        return admindisplaymenu()
    else:
        print("Please type 1")

def ped():
    n= int(input("Enter the product id to edit data"))
    for i in range(len(shopping)):
        if shopping[i]['id'] == n:
            new_offer = int(input("Enter Discount : "))
            new_price = int(input("Enter the  price : "))
            shopping[i]['Offer%'] = new_offer
            shopping[i]['Price']=new_price
            print("Data editted Successfully")
            log4=input("To return merchant page press 1 :")
            if(log4=="1"):
             return merchlogin()
            else:
                print("Please type 1")
            
            


def tpa():
    Total = 0
    print("\n")
    for d in shopping:
        print(f'{d["Name"]} = {d["Available"]}')
        Total += (d["Available"])
    print("\nTotal available goods is : ", Total)

    logtpa=input("To return to Merchant login press 1 :")
    if(logtpa=="1"):
        return merchlogin()
    else:
        print("Please type 1")

def toti():
    total = 0
    for d in shopping:
        total += ((d["Available"] * d["Price"]) - (d["Available"] * d["Original_Price"]))
    print("\nTotal income is : ", total)

    logt=input("To view Display Menu press 1 :")
    if(logt=="1"):
        return merchlogin()
    else:
        print("Please type 1")


def admindisplaymenu():
    print("")
    print("Id\tName\t\tAvailable\tPrice\tOriginal Price\tOffer%")
    for d in shopping:
        print(f'{d["id"]}\t{d["Name"]}\t\t{d["Available"]}\t\t{d["Price"]}\t{d["Original_Price"]}\t\t{d["Offer%"]}\t')

    logd=input("To return to Merchant page press 1 :")
    if(logd=="1"):
        return merchlogin()
    else:
        print("Please type 1")
        return admindisplaymenu()

def exitadminhome():
    os.system('cls')
    return home()

def exithome():
    os.system('cls')
    return home()

def exitportal():
    os.system('cls')
    print("Thank you for Shopping with A-cart 😝 ")
    print("We are glad to work for you 😍")



def idgenerator():
    global id
    id=id+1
    return id

def useridgenerator():
    global idu
    idu=idu+1
    return idu

def ordernumber():
    global order_number
    order_number=order_number+1
    return order_number


def ulogin():
    os.system('cls')
    print("")
    print("Welcome to A-cart")
    print("")
    print("1. Login")
    print("2. Signup")
    print("3. Exit")

    n=int(input("Enter your choice:"))
    if(n==1):
        login()
    elif(n==2):
        signup()
    elif(n==3):
        exithome()
    else:
        print("Invalid input")
        return home()

def login():
    global count
    os.system('cls')
    print("A-cart's Login page")
    print("")
    uname=input("Enter name : ")
    upassword=input("Enter password:")
    print("")
    for i in user:
        if((i['name']==uname) and (i['password']==upassword)):
            return userlogin(uname)
    else: 
        print("No user found")      
        logloin=input("To sign-in as new customer press S :")
        if(logloin=="S") or (logloin=="s"):
            return signup()
        count+=1
        if(count==3):
            print("")
            print("Too many wrong attempts")
            print("")
        else:
            return home()
    
def signup():
    global user
    os.system('cls')
    print("Create a new account")
    v=useridgenerator()
    print("Your id is",v)
    print("")
    nname=input("Enter name:")
    npass=input("Enter password:")
    y={'id':v,"name":nname,"password":npass}
    user.append(y)
    print("Account created Successfully")
    print("")
    print("Please return to user page & login")
    print("")
    logsig=input("To return user home press 1 :")
    if(logsig=="1"):
        return ulogin()
    else:
        print("Please type 1")

def userdisplaymenu():
    print("Id\tName\tAvailable\tPrice")
    print("")
    for d in shopping:
        print(f'{d["id"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["Price"]}')

def dispm(uname):
    global order
    global order_number
    os.system('cls')
    b=ordernumber()
    print("Id\tName\tAvailable\tPrice")
    print("")
    for d in shopping:
        print(f'{d["id"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["Price"]}')
    p_id=int(input("Enter the id of product you are interested in : "))

    for d in shopping:
        if d["id"] == p_id:
            print("\nId\tName\tAvailable\tPrice")
            print("")
            print(f'{d["id"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["Price"]}')
            
    confirm = input("\nDo you want to place an order(P) or Add to cart(A) on the above shown product : P/A ")
    if (confirm== 'P') or (confirm=='p'):
        x = input("\nDo you want to place an order on the above shown product : Y/N ")
                
        if x == 'Y' or x == 'y':
            order.append(d)

            print("\nSuccessfully placed the order on the product {} {}".format(d["id"], d["Name"]))
            print("Your order number is : ", b)
            d["Available"] -= 1
            logj=input("\nTo return login page press 1 \n\nTo continue shopping press 2 \n")
            if(logj=="1"):
                return userlogin(uname)
            elif(logj=="2"):
                return dispm(uname)
            else:
                print("Please type 1 or 2")
                return userlogin(uname)

        elif x == 'N' or x == 'n':
            print("The order is not placed. You can carry on with you purchase. \nHappy shopping!!!!")
            logj=input("\nTo return login page press 1 \n\nTo continue shopping press 2 \n")
            if(logj=="1"):
                return userlogin(uname)
            elif(logj=="2"):
                return dispm()
            else:
                print("Please type 1 or 2")
                return userlogin(uname)
        else:
            print("\nYou have entered wrong option. Please enter again\n")
            confirm = input("\nDo you want to place an order on the above shown product : Y/N ")
            
            
    elif(confirm=='A') or (confirm=='a'):
        os.system('cls')
        for d in shopping:
                print(f'{d["id"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["Price"]}')
        n=int(input("Enter number of items to Add to cart"))
        for i in range(n):
                z=int(input('Enter the id of product you want to add to cart : '))
                for d in shopping:
                    if d["id"] == z:
                        kart.append(d)
                        print("\nId\tName\tAvailable\tPrice")
                        print("")
                        print(f'{d["id"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["Price"]}')

        log3=input("\nTo view Add to cart press 1 \n")
        if(log3=="1"):
            return cart(uname)
        else:
            print("Please type 1")
            return userlogin(uname)
                           


    if d["id"] != p_id:
        print("\nYou have entered invalid id. Please enter valid id\n")
        logu=input("To return user home press 1 :")
        if(logu=="1"):
            return userlogin(uname)
        logl=input("\nTo view Products menu press M \n")
        if(logl=="M") or (logl=="m"):
            return userdisplaymenu()
        else:
            print("Please type 1")
            return userlogin(uname) 

def his(uname):
    print("History of order")
    if len(order)==0:
        print("No history of order found")
        print("")
    for d in order:
        print("Id\tName\tAvailable\tPrice")
        print("")
        print(f'{d["id"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["Price"]}')
        log5=input("\nTo return user menu press 1 \n")
        if(log5=="1"):
            return userlogin(uname)
        else:
            print("Please type 1")
            return userlogin(uname)

def logo():
    os.system('cls')
    return home()

def cal(uname):
    global order
    os.system('cls')
    found = False
    order_id = input("Enter the order id : ")
    for d in order:
        found = d["id"] == order_id
        if found != True:
            temp.append(d)
    if len(temp) == d:
        
        print(f'{order_id} is not found')
    else:
        print("\nId\tName\tAvailable\tPrice")
        print("")
        print(f'{d["id"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["Price"]}')
        confirm = input("\nDo you really want to cancel the product? : Y/N ")

        if confirm == 'Y' or confirm == 'y':

            print("\nSuccessfully removed the product {} {}".format(d["id"], d["Name"]))
            d["Available"] += 1
            logj=input("\nTo return login page press 1 \n\nTo continue shopping press 2 \n")
            if(logj=="1"):
                return userlogin(uname)
            elif(logj=="2"):
                return dispm(uname)
            else:
                print("Please type 1 or 2")
                return userlogin(uname)

        elif confirm == 'N' or confirm == 'n':
            print("The order is not removed. You can carry on with you purchase. \nHappy shopping!!!!")
            logj=input("\nTo return login page press 1 \n\nTo continue shopping press 2 \n")
            if(logj=="1"):
                return userlogin(uname)
            elif(logj=="2"):
                return dispm()
            else:
                print("Please type 1 or 2")
                return userlogin(uname)
        #print(f'{order_id} is removed from the placed order')
        log1=input("\nTo return user login page press 1 \n")
        if(log1=="1"):
            return userlogin(uname)
        else:
            print("Please type 1")
            return userlogin(uname)

def cart(uname):
    os.system('cls')
    print("ADD TO CART")
    print("Id\tName\tAvailable\tPrice")
    print("")
    if len(kart)==0:
        print("No Product in the cart")
        print("")
        log6=input("\nTo return user login press 1\n")
        if(log6=="1"):
            return userlogin(uname)
        else:
            print("Please type 1")
            return userlogin(uname)
    for d in kart:
            print(f'{d["id"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["Price"]}')
        

    log2=input("\nTo return user login page(L) or purchase product from Cart(C)\n")

    if(log2 == "L") or (log2 == "l"):
        return userlogin(uname)

    elif(log2 =="c") or (log2 == 'C'):

        return purscart(uname)

    
def purscart(uname):
    os.system('cls')
    for d in kart:
            print(f'{d["id"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["Price"]}')
    
    b=ordernumber()
    p_id = int(input("Enter product id to purchase : "))
    for d in kart:
        if d["id"] == p_id:
            print("\nId\tName\tAvailable\tPrice")
            print("")
            print(f'{d["id"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["Price"]}')
            x = input("\nDo you want to place an order on the above shown product : Y/N ")
            if x == 'Y' or x == 'y':
                order.append(d)

                print("\nSuccessfully placed the order on the product {} {}".format(d["id"], d["Name"]))
                print("Your order number is : ", b)
                d["Available"] -= 1
                logj=input("\nTo return login page press 1 \n\nTo continue shopping press 2 \n")
                if(logj=="1"):
                    return userlogin(uname)
                elif(logj=="2"):
                    return dispm(uname)
                else:
                    print("Please type 1 or 2")
                    return userlogin(uname)

            elif x == 'N' or x == 'n':
                print("The order is not placed. You can carry on with you purchase. \nHappy shopping!!!!")
                logj=input("\nTo return login page press 1 \n\nTo continue shopping press 2 \n")
                if(logj=="1"):
                    return userlogin(uname)
                elif(logj=="2"):
                    return dispm()
                else:
                    print("Please type 1 or 2")
                    return userlogin(uname)
            else:
                print("\nYou have entered wrong option. Please enter again\n")
                confirm = input("\nDo you want to place an order on the above shown product : Y/N ")
def boomer(uname):
    global kart

    for d in kart:
        print(f'{d["id"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["Price"]}')
    
    n=int(input("Enter id to be removed"))
    hardic=kart
    for i in kart:
        if i['id'] == n:
                hardic.remove(i)
                print("Product Removed sucessfully")
    kart=hardic

    log0=input("\nTo return user login page press 1 : \n")
    if(log0 == "1"):
        return userlogin(uname)

def userlogin(uname):
    os.system('cls')
    print("Welcome" ,uname)
    print("")
    print("Enjoy carting")
    print("")
    print("1. Display Menu")
    print("2. Cancel order")
    print("3. Add to cart")
    print("4. Order history")
    print("5. Logout")

    n=int(input("Enter your choice:"))
    if(n==1):
        dispm(uname)
    elif(n==2):
        cal(uname)
    elif(n==3):
        cart(uname)
    elif(n==4):
        his(uname)
    elif(n==5):
        logo()
    else:
        print("Invalid input")
        return home()


def rem():
    os.system('cls')
    print("1. Remove the Availability of products")
    print("2. Remove a product")
    print("3. Edit the product's data")
    print("4. Exit")

    n=int(input("Enter your choice:"))
    if(n==1):
        rema()
    elif(n==2):
        remp()
    elif(n==3):
        ped()       
    elif(n==4):
        exithome()
    else:
        print("Invalid input")
        return home()

def mlogin():
    os.system('cls')
    print("Welcome to A-cart")
    print("")
    print("1. Login to your merchant account")
    print("2. Signup to your merchant account")
    print("3. Exit")

    n=int(input("Enter your choice:"))
    if(n==1):
        merl()
    elif(n==2):
        mers()
    elif(n==3):
        exithome()
    else:
        print("Invalid input")
        return home()


def adminhome():
    os.system('cls')
    print("Welcome to Admin Home page ")
    print("")
    print("1. Add merchant")
    print("2. Remove merchant")
    print("3. Approve merchant")
    print("4. List of Merchants")
    print("5. Logout")

    n=int(input("Enter your choice:"))
    if(n==1):
        addm()
    elif(n==2):
        remm()
    elif(n==3):
        appm()
    elif(n==4):
        lom()
    elif(n==5):
        exithome()
    else:
        print("Invalid input")
        return adminhome()


def home():
    os.system('cls')
    print("WELCOME to A-cart")
    print("1. Admin")
    print("2. Merchant")
    print("3. User")
    print("4. Exit")

    n=int(input("Enter your choice:"))
    if(n==1):
        adminlogin()
    elif(n==2):
        mlogin()
    elif(n==3):
        ulogin()
    elif(n==4):
        exitportal()
    else:
        print("Invalid input")

home()