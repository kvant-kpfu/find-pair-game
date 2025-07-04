import turtle
import random

t = turtle.Turtle()
screen = turtle.Screen()
turtle.listen()
screen.setup(width = 1.0, height = 1.0)
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
root.overrideredirect(1)

colors=['green','green', 'blue', 'red', 'pink', 'orange', 'lightblue', 'purple', 'salmon', 'violet','blue', 'red', 'pink', 'orange', 'lightblue', 'purple', 'salmon', 'violet']
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
card_layer_index = 0
opened_cards = []
kolvo_otkr = 0
spacingx = 75
spacingy = 130
frame_x = -150
frame_y = 100

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




def draw_ramka(x, y, color='dark red', thikness=5):
    ramka = turtle.Turtle()
    ramka.penup()
    ramka.goto(x, y)
    ramka.shape('square')
    ramka.shapesize(stretch_wid=5, stretch_len=3, outline=5)
    ramka.color(color)
    ramka.fillcolor('')
    return ramka


frame = draw_ramka(-150, 100)





def check_win():
    all_hidden = True
    for card in cards_layer:
        if card.isvisible():
            all_hidden = False
            break
    if all_hidden:
        t.penup()
        t.goto(0, 350)
        t.color("red")
        t.write("Ты молодец!", align="center", font=("Courier", 46, "bold"))
        t.hideturtle()


def move_right():
    global card_layer_index, frame_x, frame_y
    cards_layer[card_layer_index].color('black')

    if card_layer_index < 17:
        card_layer_index += 1
        while card_layer_index < 17 and not cards_layer[card_layer_index].isvisible():
            card_layer_index += 1
        frame_x += 75
    if frame_x >= 300:
        frame_x -= 75

    draw_ramka(frame_x, frame_y)



def move_left():
    global card_layer_index, frame_x, frame_y
    cards_layer[card_layer_index].color('black')

    if card_layer_index > 0:
        card_layer_index -= 1
        while card_layer_index > 0 and not cards_layer[card_layer_index].isvisible():
            card_layer_index -= 1
        frame_x -= 75
    if frame_x <= -225:
        frame_x += 75
    draw_ramka(frame_x, frame_y)


def move_down():
    global card_layer_index, frame_x, frame_y
    cards_layer[card_layer_index].color('black')

    new_index = card_layer_index + 6
    if new_index <= 17:
        card_layer_index = new_index
        while card_layer_index <= 17 and not cards_layer[card_layer_index].isvisible():
            card_layer_index += 6
            if card_layer_index > 17:
                card_layer_index -= 6
                break
        frame_y -= 130
    if frame_y <= -260:
        frame_y += 130

    draw_ramka(frame_x, frame_y)

def move_up():
    global card_layer_index, frame_x, frame_y
    cards_layer[card_layer_index].color('black')

    new_index = card_layer_index - 6
    if new_index >= 0:
        card_layer_index = new_index
        while card_layer_index >= 0 and not cards_layer[card_layer_index].isvisible():
            card_layer_index -= 6
            if card_layer_index < 0:
                card_layer_index += 6
                break
        frame_y += 130
    if frame_y >= 130:
        frame_y -= 130
    draw_ramka(frame_x, frame_y)

def enter_position():
    global opened_cards, cards_layer, card_layer_index
    cards_layer[card_layer_index].hideturtle()
    opened_cards.append(card_layer_index)
    if len(opened_cards) == 2:
        proverka()
    check_win()


def proverka():
    global opened_cards, cards_layer
    if cards[opened_cards[0]].color() == cards[opened_cards[1]].color():
        pass
    else:
        for i in opened_cards:
            cards_layer[i].showturtle()

    opened_cards.clear()




turtle.onkeypress(move_right, "Right")
turtle.onkeypress(move_down, "Down")
turtle.onkeypress(move_up, "Up")
turtle.onkeypress(move_left, "Left")
turtle.onkeypress(enter_position, "space")


screen.mainloop()
turtle.done()