import tkinter as tk
from tkinter import messagebox,StringVar,ttk
import datetime
import re
from tkinter.constants import BOTH, END, LEFT, RIGHT, VERTICAL, Y
import mysql.connector as sqlc
import sys
import tkcalendar as tkc
from tkcalendar import DateEntry
###################################################################################################################################################################
mydb = sqlc.connect(host="localhost",user="root",password="1945")
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
###########################################################################################################################################
def gotoHome(page):
    page.destroy()
    Home()
####################################################################################################################################################################
def gotoDash(page,username):
    page.destroy()
    dashboard(username)
#############################################################################################################################################
def displayexpense(dash,username):
    dash.destroy()
    display=tk.Tk()
    display.geometry('550x550')
    display.resizable(False,False)
    display.title("Expense details")
    main_frame=ttk.Frame(display)
    main_frame.pack(fill=BOTH,expand=1)
    my_canvas=tk.Canvas(main_frame)
    my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
    my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT,fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    second_frame=ttk.Frame(my_canvas)
    my_canvas.create_window((0,0),window=second_frame,anchor="nw")
    head=tk.Label(second_frame,text="Personal Expense Tracker",pady=10,font=("Impact",20),background="red",width=40).grid(row=0,column=0,columnspan=4)
    empty1=tk.Label(second_frame,text=" ").grid(row=1,column=0,columnspan=4)
    query="select* from "+username+" order by dateofexpense"
    try:
        cur.execute(query)
        rows=cur.fetchall()
    except:
        print("Error")
    col1=tk.Label(second_frame,text="S.No",font=("Times New Roman",16)).grid(row=2,column=0)
    col2=tk.Label(second_frame,text="Date",font=("Times New Roman",16)).grid(row=2,column=1)
    col3=tk.Label(second_frame,text="Expense name",font=("Times New Roman",16)).grid(row=2,column=2)
    col4=tk.Label(second_frame,text="Price",font=("Times New Roman",16)).grid(row=2,column=3)
    empty2=tk.Label(second_frame,text=" ").grid(row=3,column=0,columnspan=4)
    j=0
    k=0
    for i in (rows):
        r0=tk.Label(second_frame,text=str(k+1)+".",font=("Times New Roman",16)).grid(row=j+4,column=0)
        r1=tk.Label(second_frame,text=i[2],font=("Times New Roman",16)).grid(row=j+4,column=1)
        r2=tk.Label(second_frame,text=i[0],font=("Times New Roman",16)).grid(row=j+4,column=2)
        r3=tk.Label(second_frame,text=i[1],font=("Times New Roman",16)).grid(row=j+4,column=3)
        e=tk.Label(second_frame,text=" ").grid(row=j+2,column=0,columnspan=4)
        j=j+2
        k=k+1
    empty3=tk.Label(second_frame,text=" ").grid(row=j+4,column=0,columnspan=4)
    Back=tk.Button(second_frame,text="Back",padx=10,width=7,bg="red",font=("Times New Roman",12),command=lambda:gotoDash(display,username)).grid(row=j+5,column=0,columnspan=2)
    Logout=tk.Button(second_frame,text="Logout",padx=10,width=7,bg="red",font=("Times New Roman",12),command=lambda:gotoHome(display)).grid(row=j+5,column=2,columnspan=2)
    empty4=tk.Label(second_frame,text=" ").grid(row=j+6,column=0,columnspan=4)
    display.mainloop()
#########################################################################################################################################
def displayexpensemonth(dash,username):
    dash.destroy()
    display_month=tk.Tk()
    display_month.geometry('550x550')
    display_month.resizable(False,False)
    display_month.title("Expense details")
    main_frame=ttk.Frame(display_month)
    main_frame.pack(fill=BOTH,expand=1)
    my_canvas=tk.Canvas(main_frame)
    my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
    my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT,fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    second_frame=ttk.Frame(my_canvas)
    my_canvas.create_window((0,0),window=second_frame,anchor="nw")

    months=["January","February","March","April","May","June","July","August","September","October","November","December"]
    opm=StringVar(second_frame)
    opm.set(months[0])

    years=[]
    query="select distinct(year(dateofexpense)) from "+username
    cur.execute(query)
    years=cur.fetchall()
    opy=StringVar(second_frame)
    opy.set(years[0])

    head=tk.Label(second_frame,text="Personal Expense Tracker",pady=10,font=("Impact",20),background="red",width=40).grid(row=0,column=0,columnspan=3)
    empty1=tk.Label(second_frame,text=" ").grid(row=1,column=0,columnspan=3)

    yearlabel= tk.Label(second_frame,text="Enter year :- ",font=("Times New Roman",16)).grid(row=2,column=0,sticky='w')
    yearinput= tk.OptionMenu(second_frame,opy,*years)
    yearinput.config(width=10,font=("Times New Roman",16))
    yearinput.grid(row=2,column=1)
    
    monthlabel= tk.Label(second_frame,text="Enter month :- ",font=("Times New Roman",16)).grid(row=3,column=0,sticky='w')
    monthinput= tk.OptionMenu(second_frame,opm,*months)
    monthinput.config(width=10,font=("Times New Roman",16))
    monthinput.grid(row=3,column=1)
    
    m=opm.get()
    y=opy.get()
    y=y.replace("(","")
    y=y.replace(")","")
    y=y.replace(",","")

    print(m,y)
    q="select expensename, sum(price) from "+username+" where MONTH(dateofexpense)="+str(months.index(m)+1)+" where YEAR(dateofexpense)="+str(y)+"group by(expensename);"
    empty2=tk.Label(second_frame,text=" ").grid(row=4,column=0,columnspan=3)
    enterbutton=tk.Button(second_frame,text="Display",padx=10,width=7,bg="red",font=("Times New Roman",12)).grid(row=5,column=1)
    empty3=tk.Label(second_frame,text=" ").grid(row=7,column=0,columnspan=3)
    col1=tk.Label(second_frame,text="S.No",font=("Times New Roman",16)).grid(row=8,column=0,sticky='w')
    col2=tk.Label(second_frame,text="Expense name",font=("Times New Roman",16)).grid(row=8,column=1,sticky='w')
    col3=tk.Label(second_frame,text="Amount",font=("Times New Roman",16)).grid(row=8,column=2,sticky='w')
    empty4=tk.Label(second_frame,text=" ").grid(row=9,column=0,columnspan=3)
    cur.execute(q)

######################################################################################################################################################################
def submitexpense(enter,username,expensenameInput,expenseamountInput,expensedateInput):
    name=expensenameInput.get()
    amount=expenseamountInput.get()
    date=expensedateInput.get_date()
    username.replace("\'","")
    cur.execute("use miniproject")
    sql="insert into "+username+"(expensename, price, dateofexpense) values(%s,%s,%s)"
    cur.execute(sql,(name,amount,date))
    cur.execute("commit")
    messagebox.showinfo("Data saved","Your data entered successfully")
    enter.destroy()
    dashboard(username)
#########################################################################################################################################################################
def resetexpense(expensenameInput,expenseamountInput,expensedateInput):
    try:
        expenseamountInput.delete(0,END)
    except:
        pass
####################################################################################################################################################################
def enterexpense(dash,username):
    dash.destroy()
    choice =["Food","Groceries","EMI","RENT","EB bill","Gas bill","Water","Shopping","Movies","Tour","Snacks","WIFI","Others"]
    enter=tk.Tk()
    enter.geometry('500x500')
    enter.title(username)
    enter.resizable(False,False)
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

    submitbutton= tk.Button(enter,text="Submit",font=("Times New Roman",16),bg="red",command=lambda: submitexpense(enter,username,opt,expenseamountInput,expensedateInput)).grid(row=11,column=0)
    resetbutton=  tk.Button(enter,text="Reset", font=("Times New Roman",16),bg="red",command=lambda: resetexpense(expensenameInput,expenseamountInput,expensedateInput)).grid(row=11,column=1)

    enter.mainloop()
########################################################################################################################################################################
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
#############################################################################################################################################################
def login(home,username,password):
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
############################################################################################################################################################
def reset(nameInput,emailInput,pnoInput,incomeInput,pwInput,cpwInput):
    nameInput.delete(0,END)
    emailInput.delete(0,END)
    pnoInput.delete(0,END)
    incomeInput.delete(0,END)
    pwInput.delete(0,END)
    cpwInput.delete(0,END)
###########################################################################################################################################
#Signup page
def signuppage(home):

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
    Label1= tk.Label(dash,text="    Add an expense:- ",font=("Times New Roman",16)).grid(row=2,column=0,sticky='w')
    Insert=tk.Button(dash,text="Enter",padx=10,width=7,bg="red",font=("Times New Roman",12),command=lambda: enterexpense(dash,username)).grid(row=2,column=1)
    empty2=tk.Label(dash,text=" ").grid(row=3,column=0)
    Label2= tk.Label(dash,text="    Show all the expenses:- ",font=("Times New Roman",16)).grid(row=4,column=0,sticky='w')
    Showall=tk.Button(dash,text="Enter",padx=10,width=7,bg="red",font=("Times New Roman",12),command=lambda: displayexpense(dash,username)).grid(row=4,column=1)
    empty3=tk.Label(dash,text=" ").grid(row=5,column=0)
    Label3= tk.Label(dash,text="    Show all expenses by day:- ",font=("Times New Roman",16)).grid(row=6,column=0,sticky='w')
    ShowByDay=tk.Button(dash,text="Enter",padx=10,width=7,bg="red",font=("Times New Roman",12)).grid(row=6,column=1)
    empty3=tk.Label(dash,text=" ").grid(row=7,column=0)
    Label4= tk.Label(dash,text="    Show all expenses by month:- ",font=("Times New Roman",16)).grid(row=8,column=0,sticky='w')
    ShowByMonth=tk.Button(dash,text="Enter",padx=10,width=7,bg="red",font=("Times New Roman",12),command=lambda: displayexpensemonth(dash,username)).grid(row=8,column=1)
    empty3=tk.Label(dash,text=" ").grid(row=9,column=0)
    Label5= tk.Label(dash,text="    Back to login page:- ",font=("Times New Roman",16)).grid(row=10,column=0,sticky='w')
    Back=tk.Button(dash,text="Enter",padx=10,width=7,bg="red",font=("Times New Roman",12),command=lambda:gotoHome(dash)).grid(row=10,column=1)
    empty4=tk.Label(dash,text=" ").grid(row=11,column=0)
    Label6= tk.Label(dash,text="    Exit:- ",font=("Times New Roman",16)).grid(row=12,column=0,sticky='w')
    Exit=tk.Button(dash,text="Enter",padx=10,width=7,bg="red",font=("Times New Roman",12),command=lambda: sys.exit(0)).grid(row=12,column=1)
    empty5=tk.Label(dash,text=" ").grid(row=13,column=0)
    dash.mainloop()
####################################################################################################################################
#Home page
def Home():
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
    Login=tk.Button(home,text="Login",padx=10,width=5,bg="red",command=lambda: login(home,Username,Password)).grid(row=6,column=0,columnspan=2)
    empty3=tk.Label(home,text=" ").grid(row=7,column=0,columnspan=2)
    orlabel=tk.Label(home,text="or",font=("Times New Roman",16)).grid(row=8,column=0,columnspan=2)
    empty4=tk.Label(home,text=" ").grid(row=9,column=0,columnspan=2)
    Label3=tk.Label(home,text="New user, click sign up button",font=("Times New Roman",16)).grid(row=10,column=0,columnspan=2)
    empty5=tk.Label(home,text=" ").grid(row=11,column=0,columnspan=2)
    Signup=tk.Button(home,text="Sign up",padx=10,width=5,bg="red",command=lambda: signuppage(home)).grid(row=12,column=0,columnspan=2)
    home.mainloop()
#######################################################################################################################################
Home()




    