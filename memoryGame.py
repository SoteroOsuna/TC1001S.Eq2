from random import *
from turtle import *
from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
#Turtle responsable de escribir el número de taps
writer = Turtle(visible=False)
#Adición de variables de estado para número de taps y para checar que termino
state = {'mark': None, "taps": 0, 'done': False}
hide = [True] * 64

def checkOver():
    state["done"] = True
    for index in range(64):
        if hide[index]:
            state["done"] = False
    return state["done"]

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
    if inside(x, y) and not state["done"]:
        spot = index(x, y)
        mark = state['mark']

        if mark is None or mark == spot or tiles[mark] != tiles[spot] and hide[spot]:
            state['mark'] = spot
        else:
            hide[spot] = False
            hide[mark] = False
            state['mark'] = None

        state["taps"] += 1

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

    if mark is not None and (hide[mark]):
        x, y = xy(mark)
        up()
        #Centrado de número al "voletar" tarjetas
        goto(x + 25, y + 10)
        color('black')
        write(tiles[mark], font=('Arial', 25, 'normal'), align='center')

    update()

    if checkOver():
        return

    ontimer(draw, 100)

shuffle(tiles)
setup(500, 500, 370, 0)
tracer(False)
writer.goto(0, 210)
writer.color('blue')
writer.write(state["taps"], font=("Arial", 30, 'bold'), align='center')
addshape(car)
hideturtle()
onscreenclick(tap)
draw()
done()
