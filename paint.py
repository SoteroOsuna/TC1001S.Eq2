from turtle import *
from freegames import vector

def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

#Dibujo de círculo tomando como diámetro la distancia entre los dos clicks y usando la función circle()
def drawCircle(start, end):
    "Draw circle from start to end."
    up()
    goto(start.x, start.y)
    midpoint= (start.x + end.x) / 2
    goto(midpoint, start.y - (end.x - midpoint))
    down()
    begin_fill()

    circle(end.x - midpoint)


    end_fill()
    pass  # TODO

#Función que hace un rectángulo considerando el código para el cuadrado, pero con la mitad de la altura
def rectangle(start, end):
    "Draw rectangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        if (count % 2 == 1):
            forward((end.x - start.x)/2)
        else:
            forward(end.x -start.x)
        left(90)

    end_fill()
    pass  # TODO

#Función de triángulo usando giros de 120 grados para que se devuelva al punto inicial formando un triángulo, sumando 180º interiores
def triangle(start, end):
    "Draw triangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(3):
        forward(end.x - start.x)
        left(120)

    end_fill()
    pass  # TODO

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
#Color extra: morado
onkey(lambda: color('purple'), 'P')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', drawCircle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
