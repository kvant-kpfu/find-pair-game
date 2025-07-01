import turtle
import random

t = turtle.Turtle()
screen = turtle.Screen()
turtle.listen()
colors=['green','green', 'blue', 'red', 'pink', 'orange', 'lightblue', 'purple', 'grey', 'violet','blue', 'red', 'pink', 'orange', 'lightblue', 'purple', 'grey', 'violet']
random.shuffle(colors)
def create_card(x, y, color):
    card = turtle.Turtle()
    card.penup()
    card.goto(x, y)
    card.shape('square')
    card.shapesize(stretch_wid=5, stretch_len=3)
    card.color(color)
    return card

cards = []
cards_layer = []
card_layer_index=0
spacingx = 75
spacingy = 130

for vert in range(3):
    for gor in range(6):
        x = gor * spacingx - 150
        y = -vert * spacingy + 100
        cards.append(create_card(x, y, colors.pop()))
for vert in range(3):
    for gor in range(6):
        x = gor * spacingx - 150
        y = -vert * spacingy + 100
        cards_layer.append(create_card(x, y, 'black'))

cards_layer[0].color('darkgrey')
def check_win():
    all_hidden = True
    for card in cards_layer:
        if card.isvisible():
            all_hidden = False
            break
    if all_hidden:
        t.penup()
        t.goto(0, 0)
        t.color("red")
        t.write("Ты молодец!", align="up", font=("Courier", 46, "bold"))
        t.hideturtle()

def move_right():
    global card_layer_index
    cards_layer[card_layer_index].color('black')

    if card_layer_index < 17:
        card_layer_index += 1
        while card_layer_index < 17 and not cards_layer[card_layer_index].isvisible():
            card_layer_index += 1

    cards_layer[card_layer_index].color('darkgrey')


def move_left():
    global card_layer_index
    cards_layer[card_layer_index].color('black')

    if card_layer_index > 0:
        card_layer_index -= 1
        while card_layer_index > 0 and not cards_layer[card_layer_index].isvisible():
            card_layer_index -= 1

    cards_layer[card_layer_index].color('darkgrey')


def move_down():
    global card_layer_index
    cards_layer[card_layer_index].color('black')

    new_index = card_layer_index + 6
    if new_index <= 17:
        card_layer_index = new_index
        while card_layer_index <= 17 and not cards_layer[card_layer_index].isvisible():
            card_layer_index += 6
            if card_layer_index > 17:
                card_layer_index -= 6
                break

    cards_layer[card_layer_index].color('darkgrey')


def move_up():
    global card_layer_index
    cards_layer[card_layer_index].color('black')

    new_index = card_layer_index - 6
    if new_index >= 0:
        card_layer_index = new_index
        while card_layer_index >= 0 and not cards_layer[card_layer_index].isvisible():
            card_layer_index -= 6
            if card_layer_index < 0:
                card_layer_index += 6
                break

    cards_layer[card_layer_index].color('darkgrey')
def move_position():
    cards_layer[card_layer_index].hideturtle()
    check_win()


turtle.onkeypress(move_right, "Right")
turtle.onkeypress(move_down, "Down")
turtle.onkeypress(move_up, "Up")
turtle.onkeypress(move_left, "Left")
turtle.onkeypress(move_position,"space")



screen.mainloop()
turtle.done()