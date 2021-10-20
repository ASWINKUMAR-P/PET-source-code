import tkinter as tk
import datetime as dt

dash=tk.Tk()
dash.geometry('500x500')
dash.resizable(False,False)
dash.title("Home page")

headLabel=tk.Label(dash,text="PERSONAL EXPENSE TRACKER",background="red",pady=10,font=("Impact",20),width=40).grid(row=0,column=0,columnspan=2)

empty1=tk.Label(dash,text=" ").grid(row=1,column=0)

Label1= tk.Label(dash,text="Add an expense:- ",font=("Times New Roman",16)).grid(row=2,column=0,sticky='w')
Insert=tk.Button(dash,text="Enter",padx=10,width=7,bg="red",font=("Times New Roman",12)).grid(row=2,column=1)

empty2=tk.Label(dash,text=" ").grid(row=3,column=0)

Label2= tk.Label(dash,text="Delete an expense:- ",font=("Times New Roman",16)).grid(row=4,column=0,sticky='w')
Delete=tk.Button(dash,text="Enter",padx=10,width=7,bg="red",font=("Times New Roman",12)).grid(row=4,column=1)

empty3=tk.Label(dash,text=" ").grid(row=5,column=0)

Label3= tk.Label(dash,text="Show all expenses by day:- ",font=("Times New Roman",16)).grid(row=6,column=0,sticky='w')
ShowByDay=tk.Button(dash,text="Enter",padx=10,width=7,bg="red",font=("Times New Roman",12)).grid(row=6,column=1)

empty3=tk.Label(dash,text=" ").grid(row=7,column=0)

Label4= tk.Label(dash,text="Show all expenses by month:- ",font=("Times New Roman",16)).grid(row=8,column=0,sticky='w')
ShowByMonth=tk.Button(dash,text="Enter",padx=10,width=7,bg="red",font=("Times New Roman",12)).grid(row=8,column=1)

empty3=tk.Label(dash,text=" ").grid(row=9,column=0)

dash.mainloop()
