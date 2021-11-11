import tkinter as tk
from tkinter import messagebox,StringVar,ttk
import datetime
import re
from tkinter.constants import ALL, BOTH, END, LEFT, RIGHT, VERTICAL, Y
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
username = "Aswin_P"
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
empty1=tk.Label(second_frame,text=" ").grid(row=3,column=0,columnspan=4)
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
display.mainloop()