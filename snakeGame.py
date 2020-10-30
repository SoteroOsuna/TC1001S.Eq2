from turtle import *
import random
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

#Adición de colores y loop para asegurarse de que no se repitan
colors = ['blue', 'green', 'black', 'yellow', 'purple', 'cyan', 'pink']
snakeColor = random.choice(colors)
foodColor = random.choice(colors)
while (foodColor == snakeColor):
    foodColor = random.choice(colors)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, snakeColor)

    square(food.x, food.y, 9, foodColor)
    update()
    ontimer(move, 100)

#Función para que se mueva la comida
def moveFood():

    #Código para que sólo se mueva en 4 direcciónes (arriba, abajo, izquierda y derecha) junto con limites para que se quede dentro
    opcion = randrange(0,2)
    if(opcion == 0):
        if (food.x == -200):
            food.x += 10
        elif (food.x == 190):
            food.x -= 10
        else:
            food.x += randrange(-10, 11, 20)
    else:
        if(food.y == -200):
            food.y += 10
        elif(food.y == 190):
            food.y -= 10
        else:
            food.y += randrange(-10, 11, 20)

    ontimer(moveFood, 500)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
moveFood()
done()
