import turtle
import random
import time


t = turtle.Turtle()
screen=turtle.Screen()
turtle.listen()
screen = turtle.Screen()
screen.setup(width = 1.0, height = 1.0)
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
root.overrideredirect(1)

# --- Таймер ---
timer_turtle = turtle.Turtle()
timer_turtle.hideturtle()
timer_turtle.penup()
timer_turtle.goto(0, 400)
timer_turtle.color('blue')
start_time = time.time()
timer_running = True
timer_value = 0

def update_timer():
    global timer_value, timer_running
    if timer_running:
        timer_value = int(time.time() - start_time)
        timer_turtle.clear()
        timer_turtle.write(f"Время: {timer_value} сек", align="center", font=("Courier", 24, "bold"))
        screen.ontimer(update_timer, 1000)

colors = ['green', 'green', 'blue', 'red', 'pink', 'orange', 'lightblue',
          'purple', 'salmon', 'violet', 'blue', 'red', 'pink', 'orange',
          'lightblue', 'purple', 'salmon', 'violet']
random.shuffle(colors)
is_space_pressed = False


def create_card(x, y, color):
    card = turtle.Turtle()
    card.penup()


    card.goto(x,y)
    card.shape('square')
    card.shapesize(stretch_wid=10, stretch_len=6)
    card.color(color)
    return card

cards = []
cards_layer = []
card_layer_index = 0
opened_cards = []
kolvo_otkr = 0
spacingx = 150
spacingy = 260

for vert in range(3):
    for gor in range(6):
        x = gor * spacingx - 375
        y = -vert * spacingy + 250

        cards.append(create_card(x, y, colors.pop()))

for vert in range(3):
    for gor in range(6):
        x = gor * spacingx - 375
        y = -vert * spacingy + 250
        cards_layer.append(create_card(x, y, 'black'))

cards_layer[0].color('darkgrey')

def check_win():
    global timer_running
    all_hidden = True
    for card in cards_layer:
        if card.isvisible():
            all_hidden = False
            break
    if all_hidden:
        timer_running = False
        t.penup()
        t.goto(0, 350)
        t.color("red")
        # Масштабируем размер шрифта
        t.write("Ты молодец!", align="center",
                font=("Courier", int(46), "bold"))
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

def enter_position():
    global opened_cards, cards_layer, card_layer_index, is_space_pressed
    if not is_space_pressed:
        is_space_pressed=True
        cards_layer[card_layer_index].hideturtle()
        opened_cards.append(card_layer_index)
        if len(opened_cards) == 2:
            proverka()
        check_win()
        is_space_pressed = False



def proverka():
    global opened_cards, cards_layer
    if cards[opened_cards[0]].color() == cards[opened_cards[1]].color():
        pass
    else:
        time.sleep(1)
        for i in opened_cards:
            cards_layer[i].showturtle()
    opened_cards.clear()



turtle.onkeypress(move_right, "Right")
turtle.onkeypress(move_down, "Down")
turtle.onkeypress(move_up, "Up")
turtle.onkeypress(move_left, "Left")
turtle.onkeypress(enter_position, "space")

update_timer()
screen.mainloop()
turtle.done()