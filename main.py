import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pd.read_csv("50_states.csv")
states = data["state"]

print(data[data["state"] == "Florida"])
answe_score = True
while answe_score:
  answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()

  for state in states:
      if state == answer_state:
        crr_state = data[data["state"] == answer_state]
        x_position =(int(crr_state["x"]))
        y_position = (int(crr_state["y"]))
        pen = turtle.Turtle()
        pen.color('black')
        pen.pensize(2)
        pen.penup()
        pen.goto(x_position,y_position)
        pen.write(answer_state, font=("Arial", 12, "normal"))


turtle.mainloop()
      
      
    


