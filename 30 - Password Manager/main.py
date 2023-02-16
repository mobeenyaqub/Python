import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


#  ---------------------------- WEBSITE SEARCH ------------------------------- #

def search_file():
    try:
        open("password_manager.json", "r")
    except FileNotFoundError:
        messagebox.showerror(title="Unavailable", message="No record found")
    else:
        with open("password_manager.json", "r") as file:
            data = json.load(file)
            if website_textbox.get() in data:
                messagebox.showinfo(title=website_textbox.get(),
                                    message=f"\nEmail:{data[website_textbox.get()]['email']} \n\nPassword: "
                                            f"{data[website_textbox.get()]['password']}\n\n")
            else:
                messagebox.showerror(title="Unavailable", message="No record found")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password = ""
    for i in range(0, 4):
        index = random.randint(0, len(letters) - 1)
        password += letters[index]

    for i in range(0, 4):
        index = random.randint(0, len(symbols) - 1)
        password += symbols[index]

    for i in range(0, 4):
        index = random.randint(0, len(numbers) - 1)
        password += numbers[index]

    letter = []
    for i in password:
        letter.append(i)

    p = ""
    for i in range(0, len(letter)):
        index = random.randint(0, len(letter) - 1)
        p += letter[index]
        letter.pop(index)

    password_textbox.delete(0, END)
    password_textbox.insert(0, p)
    pyperclip.copy(p)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_textbox.get()
    email_username = email_username_textbox.get()
    password = password_textbox.get()
    new_data = {
        website: {
            "email": email_username,
            "password": password
        }
    }
    is_okay = False
    if len(website) == 0 or len(email_username) == 0 or len(password) == 0:
        messagebox.showerror(title="Missing fields", message="Please fill all the cells.")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"Entered details: \n\nEmail: {email_username}\n\nPassword: {password}\n\n")

    if is_ok:
        try:
            open("password_manager.json", "r")
        except FileNotFoundError:
            open("password_manager.json", "w")
        finally:
            with open("password_manager.json", "r") as password_manager_file:
                data = json.load(password_manager_file)
                data.update(new_data)

        with open("password_manager.json", "w") as password_manager_file:
            json.dump(data, password_manager_file, indent=4)

            website_textbox.delete(0, END)
            password_textbox.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
mypass_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=mypass_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_textbox = Entry(width=33)
website_textbox.focus()
website_textbox.grid(column=1, row=1, sticky="EW")

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)
email_username_textbox = Entry(width=35)
email_username_textbox.insert(END, string="your_email")
email_username_textbox.grid(column=1, row=2, columnspan=2, sticky="EW")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_textbox = Entry(width=33)
password_textbox.grid(column=1, row=3, sticky="W")

generate_password_button = Button(text="Generate Password", width=21, command=password_generator)
generate_password_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

search_button = Button(text="Search", width=21, command=search_file)
search_button.grid(column=2, row=1)
window.mainloop()
