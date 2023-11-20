from tkinter import *

THEME_COLOR = "#375362"
question = "Blah Blah Blah"

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text=f"{question}", font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        #Label
        self.score_title = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_title.grid(column=1, row=0)

        #Buttons
        true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(highlightthickness=0, image=true_img, borderwidth=0,
                               bg=THEME_COLOR, activebackground=THEME_COLOR)
        self.true_btn.grid(column=0, row=2)

        false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(highlightthickness=0, image=false_img, borderwidth=0,
                                bg=THEME_COLOR, activebackground=THEME_COLOR)
        self.false_btn.grid(column=1, row=2)

        self.window.mainloop()
