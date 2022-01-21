import os
import random
count = 0
seats=5
Passengers=[{'name':'sabari','password':'1234','mobile':'7339408020'}]
trains=("coimbatore","Coimbatore","tirupur","Tirupur","dindugal","Dindugal","madurai","Madurai","kovilpatti","Kovilpatti")
station=10
seat_array=[[0 for j in range(station)] for i in range(seats)]
wait=[]

#cbe=
#tip=
#din=
#mdu=
#kvp=

def ticket_reservation():
    global seats
    os.system('cls')
    print("\n\n Welcome to Reservation portal \n")
    for i in seat_array:
        print(*i)
    n=int(input("Enter number seats : "))
    for pas in range(n):
        st,ed=map(int,input().split())
        for i in range(seats):
            if sum(seat_array[i][st-1:ed-1])==0:
                print("Seat Allocated is",i)
                for j in range(st-1,ed):
                    seat_array[i][j]=pas+1
                break
        else:
            wait.append([pas+1,st,ed])
            print("Seat Not Available")
    for i in seat_array:
        print(*i)  

        
def check_seat_availabilty(flag = ''):
	src = input("Enter the source station:- ")
	des = input("Enter the destination station:- ")
	flag_2 = 0
	for i in trains:
		if trains[i].src == src and trains[i].des == des:
			print("Train Name :- ",trains[i].name ," " ,"Number ",trains[i].num ," ","Day of Travel :- ",trains[i].day_of_travel)
			flag_2 += 1
	if flag_2 == 0:
		print("\nNo trains found between the stations you entered.\n")
		menu()
	if flag == '':
		train_num = acceptors.accept_train_number()
		trains[train_num].print_seat_availablity()
		menu()
	else:
		pass
def loginp():
    global count
    os.system('cls')
    print("Login page")
    print("")
    uname=input("Enter name : ")
    upassword=input("Enter password:")
    print("")
    for i in Passengers:
        if((i['name']==uname) and (i['password']==upassword)):
            return loghome()
    else: 
        print("No user found")      
        log1=input("To sign-in as new customer press S :")
        if(log1=="S") or (log1=="s"):
            return signupp()
        count+=1
        if(count==3):
            print("")
            print("Too many wrong attempts")
            print("")
        else:
            return home()

def signupp():
    global Passengers
    os.system('cls')
    print("Create a new account")
    print("")
    nname=input("Enter name : ")
    npass=input("Enter password : ")
    mobile=int(input("Enter mobile : "))
    x=str(mobile)
    if len(x)==10:
        y={"name":nname,"password":npass,"mobile":mobile}
        Passengers.append(y)
        print("Account created Successfully")
        print("")
        print("Please return to user page & login")
        print("")
    else:
        print("Please verify and Try Again")
        return signupp()
    log2=input("To return user home press 1 :")
    if(log2=="1"):
        return loginp()
    else:
        print("Please type 1")


def loghome():
    os.system('cls')
    print("\n\n Welcome to Railway Ticket Booking System\n")
    print("")
    print("1. Check PNR status")
    print("2. Ticket Reservation")
    print("3. Logout")

    n=int(input("\n\nEnter your choice : \n"))
    if(n==1):
        pnr()
    elif(n==2):
        ticket_reservation()
    elif(n==3):
        exit_home()
    else:
        print("Invalid choice")

def home():
    os.system('cls')
    print("")
    print("\n\n Welcome to Passengers login page \n")
    print("")
    print("1. Passenger login")
    print("2. Passenger sign up")
    print("3. Logout")

    n=int(input("\n\nEnter your choice : \n"))
    if(n==1):
        loginp()
    elif(n==2):
        signupp()
    elif(n==3):
        exit_all()
    else:
        print("Invalid choice")

home()

    