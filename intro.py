import tkinter as tk

home=tk.Tk()
home.geometry('500x500')
home.resizable(False,False)
home.title("PET Login or Signup")

head=tk.Label(home,text="Personal Expense Tracker",pady=10,font=("Impact",20),background="red",width=40).grid(row=0,column=0,columnspan=2)
empty1=tk.Label(home,text=" ").grid(row=1,column=0,columnspan=2)

Label1=tk.Label(home,text="Enter username:-",font=("Times New Roman",16)).grid(row=2,column=0)
Username=tk.Entry(home,width=20,font=("Times New Roman",16)).grid(row=2,column=1)

empty2=tk.Label(home,text=" ").grid(row=3,column=0,columnspan=2)

Label2=tk.Label(home,text="Enter password:-",font=("Times New Roman",16)).grid(row=4,column=0)
Password=tk.Entry(home,width=20,font=("Times New Roman",16),show="*").grid(row=4,column=1)

empty2=tk.Label(home,text=" ").grid(row=5,column=0,columnspan=2)

Login=tk.Button(home,text="Login",padx=10,width=5,bg="red").grid(row=6,column=0,columnspan=2)
empty3=tk.Label(home,text=" ").grid(row=7,column=0,columnspan=2)

orlabel=tk.Label(home,text="or",font=("Times New Roman",16)).grid(row=8,column=0,columnspan=2)
empty4=tk.Label(home,text=" ").grid(row=9,column=0,columnspan=2)

Label3=tk.Label(home,text="New user, click sign up button",font=("Times New Roman",16)).grid(row=10,column=0,columnspan=2)
empty5=tk.Label(home,text=" ").grid(row=11,column=0,columnspan=2)

Signup=tk.Button(home,text="Sign up",padx=10,width=5,bg="red").grid(row=12,column=0,columnspan=2)

home.mainloop()