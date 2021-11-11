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
username ="Albz"

display=tk.Tk()
display.geometry('510x510')
display.resizable(False,False)
display.title("PET Login or Signup")
head=tk.Label(display,text="Personal Expense Tracker",pady=10,font=("Impact",20),background="red",width=40).grid(row=0,column=0,columnspan=4)
empty1=tk.Label(display,text=" ").grid(row=1,column=0,columnspan=4)
try:
    cur.execute("select * from Aswin_P")
    rows=cur.fetchall()
except:
    print("Error")
col1=tk.Label(display,text="S.No",font=("Times New Roman",16)).grid(row=2,column=0)
col2=tk.Label(display,text="Date",font=("Times New Roman",16)).grid(row=2,column=1)
col3=tk.Label(display,text="Expense name",font=("Times New Roman",16)).grid(row=2,column=2)
col4=tk.Label(display,text="Price",font=("Times New Roman",16)).grid(row=2,column=3)
empty1=tk.Label(display,text=" ").grid(row=3,column=0,columnspan=4)
j=0
k=0
for i in (rows):
    r0=tk.Label(display,text=str(k+1)+".",font=("Times New Roman",16)).grid(row=j+4,column=0)
    r1=tk.Label(display,text=i[2],font=("Times New Roman",16)).grid(row=j+4,column=1)
    r2=tk.Label(display,text=i[0],font=("Times New Roman",16)).grid(row=j+4,column=2)
    r3=tk.Label(display,text=i[1],font=("Times New Roman",16)).grid(row=j+4,column=3)
    e=tk.Label(display,text=" ").grid(row=j+2,column=0,columnspan=4)
    j=j+2
    k=k+1

display.mainloop()