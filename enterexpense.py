import tkinter as tk
from tkinter import ttk
from tkinter.constants import END
from tkinter import StringVar, messagebox
import datetime
import re
import tkcalendar as tkc

choice =["Food","Groceries","EMI","RENT","EB bill","Gas bill","Water","Shopping","Movies","Tour","Snacks","WIFI","Others"]

def submit(expensenameInput,expenseamountInput,expensepriceInput):
    pass
def reset(expensenameInput,expenseamountInput,expensepriceInput):
    try:
        expenseamountInput.delete(0,END)
    except:
        pass

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