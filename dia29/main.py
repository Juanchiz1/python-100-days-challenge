import random

from tkinter import *
from tkinter import messagebox
#import pyperclip





# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    password_entry.insert(0, password)
    #password.pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    web_e=str(website_entry.get())
    email_e=str(email_entry.get())
    password_e=str(password_entry.get())

    if len(web_e)==0 or len(email_e)==0 or len(password_e)==0:
        messagebox.showerror("Error", "Please fill all fields")

    else:
        is_ok=messagebox.askokcancel(title=web_e,message=f" These are the details entered \n Email: {web_e} \n Password: {password_e} \n Is it okay to save?:  ")

        if is_ok:
            with open("data.txt", "a") as data:
                data.write(" | " + web_e + " | " + email_e + " | " + password_e + " | \n")

            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)
            print("saved")
        else:
            print("not saved")






# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("PASSWORD MANAGER")
window.geometry("470x370")
window.config(padx=50,pady=50)

canvas = Canvas(window,width=200,height=200)
pass_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=pass_img)
canvas.grid(row=0,column=1)

#Labels
website_label=Label(window,text="WEBSITE: ",fg="black")
website_label.grid(row=1,column=0)

email_label=Label(window,text="EMAIL: ",fg="black")
email_label.grid(row=2,column=0)

password_label=Label(window,text="PASSWORD: ",fg="black")
password_label.grid(row=3,column=0)

#Entries
website_entry=Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()

email_entry=Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"juanchiz@gmail.com")

password_entry=Entry(width=21)
password_entry.grid(row=3,column=1)

#Buttons
generate_password_botton=Button(text="GENERATE PASSWORD",command=password_generator)
generate_password_botton.grid(row=3,column=2)
add_button=Button(text="ADD",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)


window.mainloop()