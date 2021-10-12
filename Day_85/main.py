from tkinter import *
from tkinter import messagebox
from essential_generators import DocumentGenerator
import datetime as dt


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

window = Tk()
gen = DocumentGenerator()

START_TIME = 0
END_TIME = 0


def measure_start_time():
    global START_TIME
    generate_btn.config(
        text="End",
        highlightthickness=0,
        bg=DARK_GREEN,
        font=(FONT_NAME, 10, "bold"),
        activebackground=GREEN,
        activeforeground=GREY,
        width=16,
        border=0,
        foreground=GREY,
        command=measure_end_time,
    )
    start_time = dt.datetime.now().time()
    print(start_time)
    start_time_delta = dt.timedelta(
        hours=start_time.hour,
        minutes=start_time.minute,
        seconds=start_time.second,
    )
    START_TIME = start_time_delta


def measure_end_time():
    global END_TIME
    end_time = dt.datetime.now().time()
    end_time_delta = dt.timedelta(
        hours=end_time.hour,
        minutes=end_time.minute,
        seconds=end_time.second,
    )
    generate_btn.config(
        text="Start",
        highlightthickness=0,
        bg=DARK_GREEN,
        font=(FONT_NAME, 10, "bold"),
        activebackground=GREEN,
        activeforeground=GREY,
        width=16,
        border=0,
        foreground=GREY,
        command=measure_start_time,
    )
    print(end_time)
    END_TIME = end_time_delta
    calculate_wpm(END_TIME, START_TIME)


def calculate_wpm(end, start):
    total_time = str(end - start)
    print(total_time)
    total_words = input_area.get("1.0", END)
    print(total_words)
    word_count = len(total_words.split(" "))
    (h, m, s) = total_time.split(":")
    result = int(h) * 3600 + int(m) * 60 + int(s)
    print(word_count, result)
    wpm = round((word_count / result) * 100, 2)
    result_label = Label(
        text=f"SPEED {wpm}",
        font=(FONT_NAME, 18),
        bg=PINK,
        foreground=DARK,
    )
    result_label.grid(row=1, column=0, sticky=W, pady=2, padx=2)


paragraph = gen.paragraph() + "\n" + gen.paragraph()
paragraph_length = len(paragraph)
total_words = len(paragraph.split(" "))
print(paragraph_length, total_words)

window.title("Typing Speed Test")
window.config(padx=20, pady=20, bg=DARK)

length_label = Label(
    text=f"Text Length: {paragraph_length}",
    font=(FONT_NAME, 12),
    bg=DARK,
    foreground=DARK_GREEN,
)
length_label.grid(row=0, column=0, sticky=W, pady=2, padx=2)

word_count_label = Label(
    text=f"Word Count: {total_words}",
    font=(FONT_NAME, 12),
    bg=DARK,
    foreground=DARK_RED,
)
word_count_label.grid(row=0, column=1, sticky=E, pady=2, padx=2)


text_box = Text(window, height=16, width=100, wrap=WORD)
text_box.grid(row=2, column=0, columnspan=2)
text_box.insert("end", paragraph)
text_box.config(
    padx=5,
    pady=5,
    state="disabled",
    font=(f"{FONT_NAME} 12"),
    background=DARK,
    highlightthickness=0,
    highlightcolor=DARK,
    foreground=GREY,
)

generate_btn = Button(
    text="Start",
    highlightthickness=0,
    bg=DARK_GREEN,
    font=(FONT_NAME, 14, "bold"),
    activebackground=GREEN,
    activeforeground=GREY,
    width=16,
    border=0,
    foreground=GREY,
    command=measure_start_time,
)
generate_btn.grid(
    row=3, column=0, padx=10, pady=10, sticky="NESW", columnspan=2
)

input_area = Text(window, height=16, width=100, wrap=WORD)
input_area.grid(row=4, column=0, columnspan=2)
input_area.config(
    padx=5,
    pady=5,
    font=(f"{FONT_NAME} 12"),
    background=DARK,
    highlightthickness=0,
    highlightcolor=DARK,
    foreground=GREY,
)
window.mainloop()
