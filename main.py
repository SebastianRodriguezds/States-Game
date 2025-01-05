import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pd.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_state = []

while len(guessed_state) < 50:
  answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct", prompt="What's another state's name?" ).title()


  if answer_state in all_states:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data["state"] == answer_state]
    t.goto(state_data.x.item(), state_data.y.item())
    t.write(answer_state)
    guessed_state.append(answer_state)


turtle.mainloop()
      
      
    


