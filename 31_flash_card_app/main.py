from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# ----------------------------------- CSV -------------------------------------#
data_csv = pandas.read_csv("data/french_words.csv")
data = data_csv.to_dict(orient="records")
current_card = {}


def select_next_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_bg, image=front_img)
    flip_timer = window.after(3000, func=change_card)


def change_card():
    canvas.itemconfig(canvas_bg, image=back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


# ----------------------------------- UI SETUP ----------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=change_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
canvas_bg = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, text="", fill="black", font=('Ariel', 40, "italic"))
card_word = canvas.create_text(400, 263, text="", fill="black", font=('Ariel', 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
cross_icon = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=cross_icon, borderwidth=0, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR,
                   command=select_next_word)
wrong_btn.grid(column=0, row=1)

check_icon = PhotoImage(file="images/right.png")
right_btn = Button(image=check_icon, borderwidth=0, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR,
                   command=select_next_word)
right_btn.grid(column=1, row=1)

select_next_word()


window.mainloop()
