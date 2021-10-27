import tkinter as tk
from tkinter import messagebox,StringVar
import datetime
import re
from tkinter.constants import END
import mysql.connector as sqlc
import sys
import tkcalendar as tkc
from tkcalendar import DateEntry

mydb = sqlc.connect(host="localhost",user="root",password="Aswyog123@")
cur=mydb.cursor()
try:
    cur.execute("create database miniproject")
except:
    pass
try:
    cur.execute("use miniproject")
    cur.execute("create table userdetails(username varchar(50) primary key, emailid varchar(50) not null, phone varchar(15) not null, pass varchar(50) not null, incomepermonth int not null)")
except:
    pass

def submit(expensenameInput,expenseamountInput,expensepriceInput):
    pass
def reset(expensenameInput,expenseamountInput,expensepriceInput):
    try:
        expenseamountInput.delete(0,END)
    except:
        pass
def enterexpense():
    choice =["Food","Groceries","EMI","RENT","EB bill","Gas bill","Water","Shopping","Movies","Tour","Snacks","WIFI","Others"]
    enter=tk.Tk()
    enter.geometry('500x500')
    enter.resizable(False,False)
    enter.title("PET Login or Signup")
    head=tk.Label(enter,text="Personal Expense Tracker",pady=10,font=("Impact",20),background="red",width=40).grid(row=0,column=0,columnspan=2)
    empty1=tk.Label(enter,text=" ").grid(row=1,column=0,columnspan=2)

    opt=StringVar(enter)
    opt.set(choice[0])
    expensenameLabel=   tk.Label(enter,text="Enter expense name :- ",font=("Times New Roman",16)).grid(row=2,column=0,sticky='w')
    expensenameInput= tk.OptionMenu(enter,opt,*choice)
    expensenameInput.config(width=16,font=("Times New Roman",16))
    expensenameInput.grid(row=2,column=1,sticky='w')
    empty1=tk.Label(enter,text=" ").grid(row=3,column=0,columnspan=2)

    expenseamountlabel= tk.Label(enter,text="Enter price(in Rs.):- ",font=("Times New Roman",16)).grid(row=4,column=0,sticky='w')
    expenseamountInput= tk.Entry(enter,width=18,font=("Times New Roman",18))
    expenseamountInput.grid(row=4,column=1,sticky='w')
    empty1=tk.Label(enter,text=" ").grid(row=5,column=0,columnspan=2)

    expensedatelabel= tk.Label(enter,text="Select date :- ",font=("Times New Roman",16)).grid(row=6,column=0,sticky='w')
    expensedateInput= tkc.DateEntry(enter,width=18,font=("Times New Roman",16))
    expensedateInput.grid(row=6,column=1,sticky='w')
    empty1=tk.Label(enter,text=" ").grid(row=8,column=0,columnspan=2)
    empty2=tk.Label(enter,text=" ").grid(row=9,column=0,columnspan=2)
    empty3=tk.Label(enter,text=" ").grid(row=10,column=0,columnspan=2)

    submitbutton= tk.Button(enter,text="Submit",font=("Times New Roman",16),command=lambda: submit(expensenameInput,expenseamountInput,expensedateInput)).grid(row=11,column=0)
    resetbutton=  tk.Button(enter,text="Reset", font=("Times New Roman",16),command=lambda: reset(expensenameInput,expenseamountInput,expensedateInput)).grid(row=11,column=1)

    enter.mainloop()
def create(signup,nameInput,emailInput,pnoInput,incomeInput,pwInput,cpwInput):
    name=nameInput.get()
    email=emailInput.get()
    pno=pnoInput.get()
    income=incomeInput.get()
    pw=pwInput.get()    
    cpw=cpwInput.get()
    if not name or not email or not pno or not pw or not cpw or not income:
        messagebox.showwarning("Warning","Fill all the entries")
        return
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if not re.fullmatch(regex,email):
        messagebox.showwarning("Warning","Invalid emailid")
        return
    try:
        pno=int(pno)
    except:
        messagebox.showwarning("Warning","Invalid Mobile number")
        return
    if pno not in range(1000000000,9999999999):
        messagebox.showwarning("Warning","Not a valid number")
        return
    if pw!=cpw:
        messagebox.showwarning("Warning","Password is not same")
        return
    cur.execute("insert into userdetails(username, emailid, phone, incomepermonth, pass ) values (%s, %s, %s, %s, %s)",(name,email,pno,income,pw))
    cur.execute("commit")
    query="create table "+name+"(expensename varchar(20) not null, price int not null, dateofexpense date not null)"
    cur.execute(query)
    messagebox.showinfo("Account created","Your account is created successfully")
    signup.destroy()
    dashboard(name)
def login(username,password):
    un=username.get()
    pw=password.get()
    if not un or not pw:
        messagebox.showwarning("Warning","Fill all the entries")
        return
    else:
        cur.execute("use miniproject")
        cur.execute("select username,pass from userdetails")
        rows=cur.fetchall()
        f=0
        for i in rows:
            if un==i[0] and pw==i[1]:
                f=1
                break
        if f==1:
            home.destroy()
            dashboard(un)
        else:
            messagebox.showwarning("Warning","Invalid login credentials")
def reset(nameInput,emailInput,pnoInput,incomeInput,pwInput,cpwInput):
    nameInput.delete(0,END)
    emailInput.delete(0,END)
    pnoInput.delete(0,END)
    incomeInput.delete(0,END)
    pwInput.delete(0,END)
    cpwInput.delete(0,END)
###########################################################################################################################################
#Signup page
def signuppage():

    home.destroy()
    signup=tk.Tk()
    signup.title("Create your account")
    signup.geometry('500x500')
    signup.resizable(False,False)
    headLabel=tk.Label(signup,text="PERSONAL EXPENSE TRACKER",background="red",pady=10,font=("Impact",20),width=40).grid(row=0,column=0,columnspan=2)
    empty1=tk.Label(signup,text=" ").grid(row=1,column=0)
    nameLabel= tk.Label(signup,text="Enter username :- ",font=("Times New Roman",16)).grid(row=2,column=0,sticky='w')
    nameInput= tk.Entry(signup,width=18,font=("Times New Roman",16))
    nameInput.grid(row=2,column=1)
    empty1=    tk.Label(signup,text=" ").grid(row=3,column=0)
    emailLabel=tk.Label(signup,text="Enter mail-id :- ",font=("Times New Roman",16)).grid(row=4,column=0,sticky='w')
    emailInput=tk.Entry(signup,width=18,font=("Times New Roman",16))
    emailInput.grid(row=4,column=1)
    empty1=    tk.Label(signup,text=" ").grid(row=5,column=0)
    pnoLabel=  tk.Label(signup,text="Enter phone number :- ",font=("Times New Roman",16)).grid(row=6,column=0,sticky='w')
    pnoInput=  tk.Entry(signup,width=18,font=("Times New Roman",16))
    pnoInput.grid(row=6,column=1)
    empty1=    tk.Label(signup,text=" ").grid(row=7,column=0)
    income=  tk.Label(signup,text="Enter income per month :- ",font=("Times New Roman",16)).grid(row=8,column=0,sticky='w')
    incomeInput=  tk.Entry(signup,width=18,font=("Times New Roman",16))
    incomeInput.grid(row=8,column=1)
    empty1=    tk.Label(signup,text=" ").grid(row=9,column=1)
    pwLabel=   tk.Label(signup,text="Enter password :- ",font=("Times New Roman",16)).grid(row=10,column=0,sticky='w')
    pwInput=   tk.Entry(signup,width=18,font=("Times New Roman",16))
    pwInput.grid(row=10,column=1)
    empty1=    tk.Label(signup,text=" ").grid(row=11,column=0)
    cpwLabel=  tk.Label(signup,text="Confirm password :- ",font=("Times New Roman",16)).grid(row=12,column=0,sticky='w')
    cpwInput=  tk.Entry(signup,width=18,font=("Times New Roman",16))
    cpwInput.grid(row=12,column=1)
    empty1=    tk.Label(signup,text=" ").grid(row=13,column=0)
    Submit=tk.Button(signup,text="Submit",padx=10,width=7,bg="red",font=("Times New Roman",12),command=lambda: create(signup,nameInput,emailInput,pnoInput,incomeInput,pwInput,cpwInput)).grid(row=14,column=0)
    Reset =tk.Button(signup,text="Reset" ,padx=10,width=7,bg="red",font=("Times New Roman",12),command=lambda:  reset(nameInput,emailInput,pnoInput,incomeInput,pwInput,cpwInput)).grid(row=14,column=1)
    signup.mainloop()
###################################################################################################################################
#Dashboard page creation
def dashboard(username):
    cur.execute("use miniproject")
    dash=tk.Tk()
    dash.geometry('500x500')
    dash.resizable(False,False)
    dash.title(username)
    headLabel=tk.Label(dash,text="PERSONAL EXPENSE TRACKER",background="red",pady=10,font=("Impact",20),width=40).grid(row=0,column=0,columnspan=2)
    empty1=tk.Label(dash,text=" ").grid(row=1,column=0)
    Label1= tk.Label(dash,text="Add an expense:- ",font=("Times New Roman",16)).grid(row=2,column=0,sticky='w')
    Insert=tk.Button(dash,text="Enter",padx=10,width=7,bg="red",font=("Times New Roman",12)).grid(row=2,column=1)
    empty2=tk.Label(dash,text=" ").grid(row=3,column=0)
    Label2= tk.Label(dash,text="Show all the expenses:- ",font=("Times New Roman",16)).grid(row=4,column=0,sticky='w')
    Delete=tk.Button(dash,text="Enter",padx=10,width=7,bg="red",font=("Times New Roman",12)).grid(row=4,column=1)
    empty3=tk.Label(dash,text=" ").grid(row=5,column=0)
    Label3= tk.Label(dash,text="Show all expenses by day:- ",font=("Times New Roman",16)).grid(row=6,column=0,sticky='w')
    ShowByDay=tk.Button(dash,text="Enter",padx=10,width=7,bg="red",font=("Times New Roman",12)).grid(row=6,column=1)
    empty3=tk.Label(dash,text=" ").grid(row=7,column=0)
    Label4= tk.Label(dash,text="Show all expenses by month:- ",font=("Times New Roman",16)).grid(row=8,column=0,sticky='w')
    ShowByMonth=tk.Button(dash,text="Enter",padx=10,width=7,bg="red",font=("Times New Roman",12)).grid(row=8,column=1)
    empty3=tk.Label(dash,text=" ").grid(row=9,column=0)
    dash.mainloop()
####################################################################################################################################
#Login Page
home=tk.Tk()
home.geometry('500x500')
home.resizable(False,False)
home.title("PET Login or Signup")
head=tk.Label(home,text="Personal Expense Tracker",pady=10,font=("Impact",20),background="red",width=40).grid(row=0,column=0,columnspan=2)
empty1=tk.Label(home,text=" ").grid(row=1,column=0,columnspan=2)
Label1=tk.Label(home,text="Enter username:-",font=("Times New Roman",16)).grid(row=2,column=0)
Username=tk.Entry(home,width=20,font=("Times New Roman",16))
Username.grid(row=2,column=1)
empty2=tk.Label(home,text=" ").grid(row=3,column=0,columnspan=2)
Label2=tk.Label(home,text="Enter password:-",font=("Times New Roman",16)).grid(row=4,column=0)
Password=tk.Entry(home,width=20,font=("Times New Roman",16),show="*")
Password.grid(row=4,column=1)
empty2=tk.Label(home,text=" ").grid(row=5,column=0,columnspan=2)
Login=tk.Button(home,text="Login",padx=10,width=5,bg="red",command=lambda: login(Username,Password)).grid(row=6,column=0,columnspan=2)
empty3=tk.Label(home,text=" ").grid(row=7,column=0,columnspan=2)
orlabel=tk.Label(home,text="or",font=("Times New Roman",16)).grid(row=8,column=0,columnspan=2)
empty4=tk.Label(home,text=" ").grid(row=9,column=0,columnspan=2)
Label3=tk.Label(home,text="New user, click sign up button",font=("Times New Roman",16)).grid(row=10,column=0,columnspan=2)
empty5=tk.Label(home,text=" ").grid(row=11,column=0,columnspan=2)
Signup=tk.Button(home,text="Sign up",padx=10,width=5,bg="red",command=signuppage).grid(row=12,column=0,columnspan=2)
#######################################################################################################################################
home.mainloop()




    