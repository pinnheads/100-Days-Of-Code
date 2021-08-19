from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "ARIAL"
current_word = {}

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526,
                bg=BACKGROUND_COLOR, highlightthickness=0)
bg_img = PhotoImage(file="./images/card_front.png")
bg_img_2 = PhotoImage(file="./images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=bg_img)
lang_text = canvas.create_text(400, 150, text="French", fill="black",
                               font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 263, text="trouve", fill="black",
                               font=(FONT_NAME, 60, "bold"))
canvas.grid(row=0, column=0, rowspan=2, columnspan=2)


def user_knows():
    global current_word
    data.remove(current_word)
    data_to_save = pandas.DataFrame(data)
    data_to_save.to_csv("./data/words_to_learn.csv", ",", index=False)
    generate_random()

def generate_random():
    global current_word
    current_word = random.choice(data)
    print(f"{type(current_word)}: {current_word}")
    french_word = current_word["French"]
    english_word = current_word["English"]
    canvas.itemconfig(canvas_img, image=bg_img)
    canvas.itemconfig(lang_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=french_word, fill="black")
    window.after(3000, change_side, english_word)


def change_side(eng_word):
    canvas.itemconfig(canvas_img, image=bg_img_2)
    canvas.itemconfig(lang_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=eng_word, fill="white")


cross_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=cross_img, highlightthickness=0,
                   border=0, command=generate_random)
wrong_btn.grid(row=2, column=0)

tick_img = PhotoImage(file="./images/right.png")
right_btn = Button(image=tick_img, highlightthickness=0,
                   border=0, command=user_knows)
right_btn.grid(row=2, column=1)

try:
    data = pandas.read_csv(
        "./data/words_to_learn.csv", ","
    ).to_dict(orient='records')
except FileNotFoundError:
    data = pandas.read_csv(
        "./data/french_words.csv", ","
    ).to_dict(orient='records')
finally:
    generate_random()
















window.mainloop()
