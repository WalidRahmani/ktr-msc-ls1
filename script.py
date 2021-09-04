from tkinter import *
from os import read
from functools import partial
import csv


#Create login interface 
def login_window():

    #Create login window
    root = Tk()

    #Customize Login window
    root.title("ktr-msc-ls1")
    root.geometry("480x360")

    #Create fields and button 
    user = Label(root, text = "user")
    user.pack()
    e_user = Entry(root)
    e_user.pack()
    password = Label(root, text = "password")
    password.pack()
    e_password = Entry(root)
    e_password.pack()
    b = Button(root ,text="Submit", command=partial(authenticator, e_user, e_password, root))
    b.pack() 
    ca = Button(root ,text="Create account", command=partial(clear_createacc, root))
    ca.pack()

    #Run tkinter
    root.mainloop()  

def create_account():
    #Create login window
    root = Tk()

    #Customize Login window
    root.title("Create account")
    root.geometry("480x360")

    id_acc = Label(root, text = "id")
    id_acc.pack()
    e_id = Entry(root)
    e_id.pack()
    password = Label(root, text = "password")
    password.pack()
    e_password = Entry(root)
    e_password.pack()
    b = Button(root ,text="Submit", command=partial(submit_account, e_id, e_password, root))
    b.pack()


def logged_window(row):
    #Create fisrt window
    root = Tk()

    #Customize window
    root.title(row[0])
    root.geometry("480x360")

    #BOX
    myCanvas = Canvas(root, width=480, height=50, bg='ivory')
    myCanvas.pack()

    library(row[0], root)
    #Create fields and button 
    logged_as = Label(myCanvas, text = "Logged as "+row[0])
    logged_as.place(x=0, y=10)
    logout_b = Button(myCanvas ,text="Logout", fg='red', command=partial(logout, root))
    logout_b.place(x=420, y=0)
    add = Button(root ,text="Add",command=partial(add_card, row))
    add.pack(side=BOTTOM)

    #Run tkinter
    root.mainloop()

def add_card(row):
    #Create fisrt window
    root = Tk()

    #Customize window
    root.title(row[0])
    root.geometry("480x360")

    #Create fields and button 
    logged_as = Label(root, text = "Logged as "+row[0])
    logged_as.place(x=0, y=10)
    name = Label(root, text = "Name")
    name.pack()
    e_name = Entry(root)
    e_name.pack()
    company = Label(root, text = "Company Name")
    company.pack()
    e_company = Entry(root)
    e_company.pack()
    email = Label(root, text = "Email address")
    email.pack()
    e_email = Entry(root)
    e_email.pack()
    phone = Label(root, text = "Telephone number")
    phone.pack()
    e_phone = Entry(root)
    e_phone.pack()
    b = Button(root ,text="Submit",command=partial(submit_data, row, e_name, e_company, e_email, e_phone, root))
    b.pack()

    
def submit_account(e_id, e_password, root):
    #Save data account
    with open('account.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([e_id.get(),e_password.get()])
    file.close()
    f = open(e_id.get()+'.csv', 'a+')  # open file in append mode
    f.close()
    root.destroy()
    login_window()

def submit_data(row, e_name, e_company, e_email, e_phone, root):
    #Submit data on the file data user
    with open(row[0]+'.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([e_name.get(),e_company.get(),
        e_email.get(), e_phone.get()
        ])
    file.close()
    root.destroy()
    logged_window(row)


def authenticator(e_user, e_password, root):
    #Verifiy if the account exist
    with open('account.csv', 'r',) as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            if e_user.get() == row[0] and e_password.get() == row[1]:
               root.destroy()
               logged_window(row)
    file.close()

def library(data,root):
    #Show all the data saved
    with open(data+'.csv', 'r',) as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            frame = Frame(root, bg='grey', bd=1)
            card = Label(frame, text = "name: "+row[0]+" company: "+row[1]+" email: "+row[2]+" phone: "+row[3])
            card.pack()
            frame.pack(expand=YES)
    file.close()
    
def clear_createacc(root):
    #Switching window
    root.destroy()
    create_account()
 
def logout(root):
    root.destroy()
    login_window()

login_window()
