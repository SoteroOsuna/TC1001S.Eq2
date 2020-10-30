from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

#OOPS

def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        #Aumento de velocidad inicial al hacer click aumentando magnitud de speed en ambas direcciones
        speed.x = (x + 400) / 20
        speed.y = (y + 400) / 20

def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    "Move ball and targets."
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        #Aumento de velocidad con aumento de magnitud
        target.x -= 2
        #Condición para reposicionar targets cuando se salgan completamente del cuadro al salirse de la posición de hasta la izquierda
        if (target.x == -220):
            target.x = 190

    if inside(ball):
        #Aumentar velocidad de caída aumentando magnitud de speed
        speed.y -= 1
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    #Hacer el juego infinito quitando la condición de que se acabe cuando un target
    '''
    for target in targets:
        if not inside(target):
            return
    '''

    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
