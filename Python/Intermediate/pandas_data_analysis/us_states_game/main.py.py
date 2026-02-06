import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
image = "/assets/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("/data/50_states.csv")
states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                              prompt="What's another state's name?").title()
    if answer.lower() == "exit":
        missing_states = [state for state in states if state not in guessed_states]
        new_data = {"States_To_Learn": missing_states}
        df = pd.DataFrame(new_data)
        df.to_csv("data/states_to_learn.csv")
        break

    if answer in states:
        guessed_states.append(answer)
        state_data = data[data.state == answer]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)