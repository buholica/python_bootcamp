from flask import Flask
import random

random_number = random.randint(1, 10)
my_higher_lower_game = Flask(__name__)


@my_higher_lower_game.route("/")
def guess_title():
    return ('<h1>Guess a number between 0 and 10</h1>'
            '<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWpuZGZyMmliYnhpd2ZnZWVrNmF2OHN1M3lrenFzNDZ2MjZhY3FyYiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/h4wTo632mUgN6ObJrc/giphy.gif" width=300>')


@my_higher_lower_game.route("/<int:user_number>")
def compare_answers(user_number):
    if user_number == random_number:
        return ('<h1 style="color: green">You found me!</h1>'
                '<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExdnFsMXhpbTQ5OTlneHl4bnNmbW9td2t6bWUyeXFiMmo4dzNoMzhyaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/o75ajIFH0QnQC3nCeD/giphy.gif" width=300>')
    elif user_number > random_number:
        return ('<h1 style="color: purple">Too high, try again!</h1>'
                '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdXJhc2N4ZTMyY250YzFmaHFteG9jcDMwOTg1ZjZjYzJuaGV0bmRmbiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/TmFvpBgG9EKFUsAG5X/giphy.gif" width=300>')
    else:
        return ('<h1 style="color: red">Too low, try again!</h1>'
                '<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExbHJwOG14NnNkbjQxYzBsNmV6NHh3cnk1NG5ibHB0NncxaGFnM3c1NiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/1r8YxFhkiBZn7NRzS5/giphy.gif" width=300>')


if __name__ == "__main__":
    my_higher_lower_game.run(debug=True)
