import pyperclip
from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
# ================================ CONSTANTS ================================ #

PINK = "#e2979c"
GREY = "#e6e6e6"
DARK_GREY = "#2e2d2d"
RED = "#d16236"
DARK_RED = "#d1342c"
GREEN = "#49912a"
DARK_GREEN = "#00A884"
DARK = "#111418"
FONT_NAME = "Courier"

# ========================== PASSWORD GENERATOR ============================= #

def generate_password():
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.insert(0, password)

# ============================= SAVE TO FILE ================================ #


def save():
    user_website = website_entry.get()
    user_email = email_entry.get()
    user_password = password_entry.get()

    if user_email == "" or user_website == "" or user_password == "":
        messagebox.showerror(title="Oops!", message="Fields cannot be empty")
        pass
    else:
        is_ok = messagebox.askokcancel(
            title=user_website,
            message=f"These are the details entered: \n\nEmail: {user_email} " +
            f"Password={user_password}\n\nIs it okay to save?"
        )
        if is_ok:
            with open("data.txt", "a+") as password_log:
                password_log.write(
                    f"{user_website} | {user_email} | {user_password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ================================ UI ======================================= #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg=DARK)

canvas = Canvas(width=200, height=200, bg=DARK, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)
# ------------------------------ LABELS ------------------------------------- #
website_label = Label(
    text="Website:", font=(FONT_NAME, 12), bg=DARK, foreground=GREY
)
website_label.grid(row=1, column=0, sticky=E, pady=2, padx=2)

email_label = Label(
    text="Email/Username:", font=(FONT_NAME, 12), bg=DARK, foreground=GREY
)
email_label.grid(row=2, column=0, sticky=E, pady=2, padx=2)

password_label = Label(
    text="Password:", font=(FONT_NAME, 12), bg=DARK, foreground=GREY
)
password_label.grid(row=3, column=0, sticky=E, pady=2, padx=2)

# ------------------------------ TEXT FIELDS -------------------------------- #
website_entry = Entry(width=44)
website_entry.config(border=0, highlightcolor=GREY, highlightthickness=1)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2, sticky=W, pady=5, padx=5)

email_entry = Entry(width=44)
email_entry.config(border=0, highlightcolor=GREY, highlightthickness=1)
email_entry.insert(0, "utsavdeep01@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2, sticky=W, pady=5, padx=5)

password_entry = Entry(width=24)
password_entry.config(border=0, highlightcolor=GREY, highlightthickness=1)
password_entry.grid(row=3, column=1, sticky=W, pady=5, padx=5)

# ------------------------------ BUTTONS ------------------------------------ #
generate_btn = Button(
    text="Generate Password", highlightthickness=0,
    bg=DARK_GREEN, font=(FONT_NAME, 10, "bold"), activebackground=GREEN,
    activeforeground=GREY, width=16, border=0, foreground=GREY,
    command=generate_password)
generate_btn.grid(row=3, column=2, sticky=W)

add_btn = Button(
    text="Add", highlightthickness=0, bg=RED,
    font=(FONT_NAME, 10, "bold"), activebackground=DARK_RED, activeforeground=GREY,
    width=41, border=0, foreground=GREY, command=save)
add_btn.grid(row=4, column=1, columnspan=2, sticky=W, padx=8, pady=8)


window.mainloop()
