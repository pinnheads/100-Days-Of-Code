from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.attributes("-type", "dialog")
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(
            text=f"Score: {self.quiz.score}",
            fg="white",
            bg=THEME_COLOR,
            font=("Arial", 12, "bold"),
        )
        self.score_label.grid(row=0, column=1, sticky=N)

        self.true_photo = PhotoImage(file="./images/true.png")
        self.false_photo = PhotoImage(file="./images/false.png")

        self.true_btn = Button(
            image=self.true_photo,
            highlightthickness=0,
            border=0,
            borderwidth=0,
            command=self.user_chose_true,
        )
        self.true_btn.grid(row=2, column=0, padx=20, pady=20)

        self.false_btn = Button(
            image=self.false_photo,
            highlightthickness=0,
            border=0,
            borderwidth=0,
            command=self.user_chose_false,
        )
        self.false_btn.grid(row=2, column=1, padx=20, pady=20)

        self.canvas = Canvas(width=400, height=350, highlightthickness=0)
        self.question_text = self.canvas.create_text(
            200,
            175,
            width=380,
            text="Question text goes here",
            font=("Arial", 20, "italic"),
        )
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=50)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(
                self.question_text,
                text=f"You've completed the quiz! Your final score was: {self.quiz.score}/{self.quiz.question_number}",
            )
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def user_chose_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def user_chose_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
