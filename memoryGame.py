from random import *
from turtle import *
from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
#Turtle responsable de escribir el número de taps
writer = Turtle(visible=False)
state = {'mark': None, "taps": 0}
hide = [True] * 64

def inside(x, y):
    return -200 < x < 200 and -200 < y < 200

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    if(inside(x, y)):
        spot = index(x, y)
        mark = state['mark']

        if mark is None or mark == spot or tiles[mark] != tiles[spot]:
            state['mark'] = spot
        else:
            hide[spot] = False
            hide[mark] = False
            state['mark'] = None

        global tapCounter
        state["taps"] += 1
        print(state["taps"])

def draw():
    "Draw image and tiles."

    #Escribir el número de taps en la pantalla
    writer.undo()
    writer.write(state["taps"], font=("Arial", 30, 'bold'), align='center')
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(500, 500, 370, 0)
tracer(False)
writer.goto(0, 210)
writer.color('blue')
writer.write(state["taps"], font=("Arial", 30, 'bold'), align='center')
listen()
addshape(car)
hideturtle()
onscreenclick(tap)
draw()
done()
