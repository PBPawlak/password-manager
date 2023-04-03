from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [choice(letters) for _ in range(randint(8, 10))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letters_list + symbols_list + numbers_list
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = user_entry.get()
    password = password_entry.get()


    if len(password) == 0 or len(website) == 0:
        messagebox.showinfo(title="Missing data",
                            message="it seems that you've left some spaces empty, please fill them")
        is_ok = False
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \nIs it ok tto save?")


    if is_ok:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password} \n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Menager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
user_id_label = Label(text="Email/Username:")
user_id_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry()
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()
user_entry = Entry()
user_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
user_entry.insert(0, "dummy@email.com")
password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="EW")

# Buttons
generate_password_btn = Button(text="Generate Password", command=generate_password)
generate_password_btn.grid(column=2, row=3)
add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
