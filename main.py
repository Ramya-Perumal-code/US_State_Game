import turtle
from turtle import Turtle

import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
count = 0
# answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
# if not answer_state is None:
#     answer_state = answer_state.title()
guess_list = []
not_guessed_list = []

while len(guess_list) < 50:
    answer_state = screen.textinput(title=f"{len(guess_list)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        not_guessed_list = [n for n in state_list if not n in guess_list]
        # for n in state_list:
        #     if not n in guess_list:
        #         not_guessed_list.append(n)
        df = pandas.DataFrame(not_guessed_list)
        df.to_csv("not_Guessed_States.csv")
        break
    if answer_state in state_list:
        df = data[data.state == answer_state]
        x_value = int(df.x.iloc[0])
        y_value = int(df.y.iloc[0])
        tim = Turtle()
        tim.hideturtle()
        tim.penup()
        tim.goto(x_value, y_value)
        tim.write(answer_state)
        guess_list.append(answer_state)

    # if not answer_state is None:
    #     answer_state = answer_state.title()
# screen.exitonclick()
