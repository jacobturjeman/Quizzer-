# THEME_COLOR = "#375362"
THEME_COLOR = "steelblue"
from quiz_brain import QuizBrain
from tkinter import *


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.user_answer: bool
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, height=500, width=400, pady=20, padx=20)
        self.score_label = Label(
                                text=f"score: {self.quiz.score}",
                                foreground="white",
                                background=THEME_COLOR,
                                padx=20, pady=20
                                )
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250,bg="white")
        self.question_text = self.canvas.create_text(
                                150, 125,
                                width=280,
                                fill="black",
                                font=("Arial", 18, "italic")
                                )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        v_image = PhotoImage(file="./images/true.png")
        x_image = PhotoImage(file="./images/false.png")
        self.v_button = Button(image=v_image, highlightthickness=0, command=self.clicked_true)
        self.v_button.grid(row=2, column=0)
        self.x_button = Button(image=x_image, highlightthickness=0, command=self.clicked_false)
        self.x_button.grid(row=2, column=1)
        self.get_question()


        self.window.mainloop()

    def get_question(self):
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())
            self.score_label.config(text=f"score: {self.quiz.score}")
            self.canvas.config(bg="white")
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text,
                                   text=f"Your final score: {self.quiz.score}/{len(self.quiz.question_list)}")

    def clicked_true(self):
        result = self.quiz.check_answer("True")
        self.give_feedback(result)

    def clicked_false(self):
        result = self.quiz.check_answer("False")
        self.give_feedback(result)

    def give_feedback(self, answer: bool):
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        # creates delay for tkinter, do not use sleep of "time"
        self.window.after(500, self.get_question)


