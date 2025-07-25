import turtle
import pandas
from text_answers import TextAnswers

screen = turtle.Screen()
screen.title("U.S. States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
data = pandas.read_csv("50_states.csv")
x = data["x"]
y = data["y"]
state = data["state"]
each_state = [(state[i], x[i], y[i]) for i in range(len(state))]


score = 0
game_is_on = True
while game_is_on:
    answer = screen.textinput(title=f"{score}/{len(state)}Guess the State", prompt="Enter states name:").title()
    if answer == "Exit":
        all_states = [st[0] for st in each_state]
        csv_file = pandas.DataFrame(all_states)
        csv_file.to_csv("States_to_learn.csv")
        break

    for st in each_state:
        if answer == st[0]:
            score += 1
            TextAnswers(st[0], st[1], st[2])
            each_state.remove(st)


screen.exitonclick()
