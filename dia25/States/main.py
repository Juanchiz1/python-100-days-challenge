import turtle

import pandas as pd

screen=turtle.Screen()
image="blank_states_img.gif"
screen.title("US STATES GAME")
screen.addshape(image)
turtle.shape(image)


def get_mouse_click_coor(x,y):
    print(x,y)

turtle.onscreenclick(get_mouse_click_coor)
guesed_states=[]

while len(guesed_states)<50:
    answer_state=screen.textinput(title=f"{len(guesed_states)}/50 States Correct",prompt="Enter a State Name: ").title()

    datos=pd.read_csv("50_states.csv")
    states_name=datos.state.tolist()

    if answer_state=="Exit":
        missing_states=[]
        for state in states_name:
            if state not in guesed_states:
                missing_states.append(state)
        missing_states_pd=pd.DataFrame(missing_states)
        missing_states_pd.to_csv("missing_states.csv")
        break
    if answer_state in states_name:
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=datos[datos.state==answer_state]
        y=state_data.y.tolist()
        x=state_data.x.tolist()
        t.goto(x[0],y[0])
        t.showturtle()
        t.write(answer_state)
        t.color("white")
        guesed_states.append(answer_state)

screen.exitonclick()


