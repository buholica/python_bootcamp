from turtle import Screen, Turtle
import pandas
import csv

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)
map_img = Turtle()
map_img.shape(image)

text = Turtle()
text.penup()
text.hideturtle()

data = pandas.read_csv("50_states.csv")
state_names = data["state"].tolist()
x_cor_list = data["x"].tolist()
y_cor_list = data["y"].tolist()


guessed_states = []
missing_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{len(state_names)} States Correct",
                                    prompt="What's another state's name?")

    if answer_state.lower() == "exit":
        for state in state_names:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    for state in state_names:
        state_l = state.lower()
        if answer_state.lower() == state_l:
            guessed_states.append(answer_state)
            index = state_names.index(state)
            x_cor = x_cor_list[index]
            y_cor = y_cor_list[index]
            text.goto(x_cor, y_cor)
            text.write(state)
