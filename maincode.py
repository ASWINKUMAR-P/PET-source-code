import mysql.connector as sqlc
import sys
import smtplib as sm
import random as ra

def emailverivication(emailid):
    email=emailid
    num=ra.randint(100000,999999)
    server=sm.SMTP_SSL("smtp.gmail.com",465)
    server.login("personalexpensetrackerforusers@gmail.com","PETminiproject")
    msg="Hello user, your OTP is "+str(num)
    server.sendmail("akthegreat003@gmail.com",email,msg)
    return num


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
    print("3. Display expense by day")
    print("4. Display expense by month")
    print("5. Display expense by year")
    print("6. Exit")
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
            print()
            f=1
            break
    if f==0:
        print("Invalid username or password")
        print()
    elif f==1:
        loginmenu(us,pw)

def signup():
    cur.execute("use miniproject")
    username=input("Enter user name:-")
    emailid=input("Enter email-id:-")
    pno=int(input("Enter phone number:-"))
    incomepermonth=int(input("Enter average income per month:-"))
    password=input("Enter password:-")
    print()
    orignalotp=emailverivication(emailid)
    print("OTP has sent in your mail.\nEnter OTP for verification")
    otp=int(input())
    if otp==orignalotp:
        cur.execute("insert into userdetails(username, emailid, phone, incomepermonth, pass ) values (%s, %s, %s, %s, %s)",(username,emailid,pno,incomepermonth,password))
        cur.execute("commit")
        print("Data entered successfully")
    else:
        print("Wrong OTP")
        print("Account not created")
    
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

    