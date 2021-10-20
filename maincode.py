import mysql.connector as sqlc
import sys
mydb = sqlc.connect(host="localhost",user="root",password="Aswyog123@")
cur=mydb.cursor()
try:
    cur.execute("create database miniproject")
except:
    pass

def loginmenu(uname,upwd):
    print("Dashboard")
    print("=========")
    print()
    print("1. Enter the expense")
    print("2. Show all expense")
    print("3. Display expense by month")
    print("4. Display expense by year")
    print("5. Exit")
    print()
    c=input("Enter your choice :-")

def login():
    us=input("Enter username:-")
    pw=input("Enter password:-")
    cur.execute("use miniproject")
    cur.execute("select username, pass from userdetails")
    f=0
    for i in cur:
        if i[0]==us and i[1]==pw:
            print("Login successful")
            f=1
            break
    if f==0:
        print("Invalid username or password")
    elif f==1:
        loginmenu(us,pw)

def signup():
    cur.execute("use miniproject")
    username=input("Enter user name:-")
    emailid=input("Enter email-id:-")
    pno=int(input("Enter phone number:-"))
    incomepermonth=int(input("Enter average income per month:-"))
    password=input("Enter password:-")
    cur.execute("insert into userdetails(username, emailid, phone, incomepermonth, pass ) values (%s, %s, %s, %s, %s)",(username,emailid,pno,incomepermonth,password))
    cur.execute("commit")
    print("Data entered successfully")
    
def loginSignupMenu():
    print("Personal Expense Tracker")
    print("1.Login")
    print("2.Signup")
    print("3.Exit")
    c=int(input("Enter your choice:-"))
    if c==1:
        login()
    elif c==2:
        signup()
    elif c==3:
        sys.exit

loginSignupMenu()

    