import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(725, 495)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
# screen.tracer(0)
# def get_mouse_click_coordinates(x, y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coordinates)

score = 0
var = []
state_over = False
while not state_over:
#     screen.update()

    answer_txt = turtle.Screen().textinput(title=f"{score}/50 Guess State", prompt="What's another state name?").title()

    data = pd.read_csv("50_states.csv")
    state_name = data[data.state == answer_txt]
    state_map = str(state_name.state)


    # If you quit all answer will shown on directly
    if answer_txt == "Quit":
        state_names = data['state'].to_list()
        for all in state_names:
            state_nome = data[data.state == all]
            x_pos = int(state_nome.x)
            y_pos = int(state_nome.y)
            turtle.penup()
            turtle.goto(x_pos, y_pos)
            turtle.write(all, align="center", font=("Ariel", 9, "bold"))
            turtle.goto(0, 0)


    if answer_txt in state_map:
        x_pos = int(state_name.x)
        y_pos = int(state_name.y)
        turtle.penup()
        turtle.goto(x_pos, y_pos)
        turtle.write(answer_txt, align="center", font=("Ariel", 9, "bold"))
        turtle.goto(0, 0)

        if answer_txt not in var:
            score += 1
        else:
            score = score


    if score == 50:
        state_over = True


    # To control over saving of states in var and help to save memory
    if answer_txt not in var:
        var.append(answer_txt)


turtle.mainloop()
