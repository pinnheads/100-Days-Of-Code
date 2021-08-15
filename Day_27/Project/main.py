from tkinter import *

window = Tk()
window.title("Miles to KM 🔢")
window.minsize(width=280, height=80)
window.config(padx=10, pady=10)

# function for the button to work


def button_click():
    global user_entry
    miles = float(user_entry.get())
    conversion = (miles) * 1.609
    num_zero.config(text=conversion)
    return conversion


# "is equal to" Label:
my_label = Label(text='Is equal to:', font=("Arial", 14, "bold"))
my_label.grid(column=0, row=1)

# "miles" label
miles_label = Label(text='Miles', font=("Arial", 14, "bold"))
miles_label.grid(column=2, row=0)

# "km" label
km_label = Label(text='Km', font=("Arial", 14, "bold"))
km_label.grid(column=2, row=1)

# 0 label
num_zero = Label(text='0', font=("Arial", 14, "bold"))
num_zero.grid(column=1, row=1)

# User entry
user_entry = Entry(width=15)
#Add some text to begin with
user_entry.insert(END, string="Enter Number")
print(user_entry.get())
user_entry.grid(column=1, row=0)

# Converter button
button = Button(text="Calculate", command=button_click)
button.grid(column=1, row=2)

# Keep the window open
window.mainloop()
