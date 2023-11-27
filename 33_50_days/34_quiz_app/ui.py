from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
question = "Blah Blah Blah"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="", font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Label
        self.score_title = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 12))
        self.score_title.grid(column=1, row=0)

        # Buttons
        true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(highlightthickness=0, image=true_img, borderwidth=0,
                               bg=THEME_COLOR, activebackground=THEME_COLOR, command=self.true_pressed)
        self.true_btn.grid(column=0, row=2)

        false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(highlightthickness=0, image=false_img, borderwidth=0,
                                bg=THEME_COLOR, activebackground=THEME_COLOR, command=self.false_pressed)
        self.false_btn.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_title.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if not is_right:
            self.canvas.config(bg="red")
        else:
            self.canvas.config(bg="green")

        self.window.after(1000, self.get_next_question)
