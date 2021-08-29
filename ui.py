import tkinter
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#FFF9E3"
SCORE_FONT = ("Arial Nova Cond", 24, "bold")
QUESTION_FONT = ("Objectivity", 18, "italic")
RESULT_FONT = ("COUTURE", 30, "normal")


class QuizInterface():

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)

        self.score_label = Label(text=f"SCORE : 0", fg="Black", font=SCORE_FONT, bg=THEME_COLOR)
        self.score_label.grid(row=0, column=2, sticky="E")

        card_front = PhotoImage(file="./images/card-front.png")
        # card_back = PhotoImage(file="./images/card-back.png")
        self.canvas = Canvas(width=616, height=405, highlightthickness=0, bg=THEME_COLOR)
        self.card_bg = self.canvas.create_image(308, 202, image=card_front)
        self.question_prompt = self.canvas.create_text(308, 202, text="Some Question", fill="black",
                                                       font=QUESTION_FONT, width=500)
        self.canvas.grid(column=1, row=1, columnspan=3, sticky="W")

        check_image = PhotoImage(file="./images/true.png")
        wrong_image = PhotoImage(file="./images/false.png")

        self.right_button = Button(image=check_image, highlightthickness=0, borderwidth=0,
                                   relief="groove", command=self.true_option)
        self.right_button.grid(row=2, column=2, sticky="W")

        self.wrong_button = Button(image=wrong_image, highlightthickness=0, borderwidth=0,
                                   relief="groove", command=self.false_option)
        self.wrong_button.grid(row=2, column=3, sticky="W")

        self.display_question()

        self.window.mainloop()

    def display_question(self):
        self.canvas.itemconfig(self.question_prompt, text="")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score : {self.quiz.score}")
            self.canvas.itemconfig(self.question_prompt, text=self.quiz.next_question(), fill="black",
                                   font=QUESTION_FONT, width=500)
        else:
            self.score_label.config(text="")
            self.canvas.itemconfig(self.question_prompt, text=f"You've reached the end of the quiz!"
                                                              f"\n\tFinal Score : {self.quiz.score}", fill="black", font=QUESTION_FONT, width=500)
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_option(self):
        self.get_solution(self.quiz.check_answer("True"))

    def false_option(self):
        self.get_solution(self.quiz.check_answer("False"))

    def get_solution(self, correct):
        if correct:
            self.canvas.itemconfig(self.question_prompt, text="CORRECT !", font=RESULT_FONT, fill="SpringGreen2")
        elif not correct:
            self.canvas.itemconfig(self.question_prompt, text="WRONG !", font=RESULT_FONT, fill="red2")
        self.window.after(1000, self.display_question)
