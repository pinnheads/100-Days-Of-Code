FONT_NAME = "Courier"
PINK = "#e2979c"
GREY = "#e6e6e6"
DARK_GREY = "#2e2d2d"
RED = "#d16236"
DARK_RED = "#d1342c"
GREEN = "#49912a"
DARK_GREEN = "#00A884"
DARK = "#111418"
FONT_NAME = "Courier"

import os
import random
from tkinter import *
from tkinter import messagebox
from image_watermark import ImageWatermark


iw = ImageWatermark()
window = Tk()
window.title("Image Watermark")
window.config(padx=20, pady=20, bg=DARK)

canvas = Canvas(width=200, height=50, bg=DARK, highlightthickness=0)
canvas.grid(row=0, column=1)

random_number = random.randint(0, 9999)

default_location = f"{os.path.expanduser('~')}/Python_Watermarked"


def get_entries():
    input_image = (
        "image.jpg"
        if input_image_entry.get() == ""
        else input_image_entry.get()
    )
    output_path = (
        default_location if output_image.get() == "" else output_image.get()
    )
    watermark_text = "Python" if text_entry.get() == "" else text_entry.get()
    output = iw.watermark_text(
        input_image,
        f"{output_path}/image_{random_number}.jpg",
        text=watermark_text,
        pos=(0, 0),
    )
    output_image.insert(0, output)
    messagebox.showinfo(title="Successfull", message=f"Image saved at {output}")


# ------------------------------ LABELS ------------------------------------- #
input_image_label = Label(
    text="Image Path", font=(FONT_NAME, 12), bg=DARK, foreground=GREY
)
input_image_label.grid(row=1, column=0, sticky=E, pady=2, padx=2)

output_image_label = Label(
    text="Output Path", font=(FONT_NAME, 12), bg=DARK, foreground=GREY
)
output_image_label.grid(row=2, column=0, sticky=E, pady=2, padx=2)

text_label = Label(
    text="Watermark Text", font=(FONT_NAME, 12), bg=DARK, foreground=GREY
)
text_label.grid(row=3, column=0, sticky=E, pady=2, padx=2)

# ------------------------------ TEXT FIELDS -------------------------------- #
input_image_entry = Entry(width=44)
input_image_entry.config(border=0, highlightcolor=GREY, highlightthickness=1)
input_image_entry.focus()
input_image_entry.grid(row=1, column=1, columnspan=2, sticky=W, pady=5, padx=5)

output_image = Entry(width=44)
output_image.config(border=0, highlightcolor=GREY, highlightthickness=1)
output_image.grid(row=2, column=1, columnspan=2, sticky=W, pady=5, padx=5)

text_entry = Entry(width=24)
text_entry.config(border=0, highlightcolor=GREY, highlightthickness=1)
text_entry.grid(row=3, column=1, sticky=W, pady=5, padx=5)

# ------------------------------ BUTTONS ------------------------------------ #
generate_btn = Button(
    text="Watermark Image",
    highlightthickness=0,
    bg=DARK_GREEN,
    font=(FONT_NAME, 10, "bold"),
    activebackground=GREEN,
    activeforeground=GREY,
    width=16,
    border=0,
    foreground=GREY,
    command=get_entries,
)
generate_btn.grid(row=3, column=2, sticky=W)

window.mainloop()
