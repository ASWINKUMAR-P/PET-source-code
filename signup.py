import tkinter as tk
from tkinter import messagebox
import datetime
import re

def create():
    name=nameInput.get()
    email=emailInput.get()
    pno=pnoInput.get()
    pw=pwInput.get()
    cpw=cpwInput.get()
    if not name or not email or not pno or not pw or not cpw:
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
    messagebox.showinfo("Account created","Your account is created successfully")
    


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

empty1=    tk.Label(signup,text=" ").grid(row=7,column=1)

pwLabel=   tk.Label(signup,text="Enter password :- ",font=("Times New Roman",16)).grid(row=8,column=0,sticky='w')
pwInput=   tk.Entry(signup,width=18,font=("Times New Roman",16))
pwInput.grid(row=8,column=1)

empty1=    tk.Label(signup,text=" ").grid(row=9,column=0)

cpwLabel=  tk.Label(signup,text="Confirm password :- ",font=("Times New Roman",16)).grid(row=10,column=0,sticky='w')
cpwInput=  tk.Entry(signup,width=18,font=("Times New Roman",16))
cpwInput.grid(row=10,column=1)

empty1=    tk.Label(signup,text=" ").grid(row=11,column=0)

Submit=tk.Button(signup,text="Submit",padx=10,width=7,bg="red",font=("Times New Roman",12),command=create).grid(row=12,column=0)
Reset =tk.Button(signup,text="Reset",padx=10,width=7,bg="red",font=("Times New Roman",12)).grid(row=12,column=1)
signup.mainloop()


