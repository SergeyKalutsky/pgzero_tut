import pgzrun
import random


TITLE = 'YOUR TITLE'
WIDTH = 640
HEIGHT = 1002

# Загрузка изображений
bg = Actor('bg2.png')
astronaut = Actor('astronaut')
asteroid1 = Actor('asteroid1')
asteroid1.pos = (200, 300)
asteroid2 = Actor('asteroid2')
asteroid2.pos = (400, 600)

x, y = 0, 0


def draw():
    bg.draw()
    astronaut.draw()
    asteroid1.draw()
    asteroid2.draw()


def update(dt):
    astronaut.x += x
    astronaut.y += y
    if astronaut.left < 0:
        astronaut.left = 0
    if astronaut.right > WIDTH:
        astronaut.right = WIDTH
    if astronaut.top < 0:
        astronaut.top = 0
    if astronaut.bottom > HEIGHT:
        astronaut.bottom = HEIGHT


def on_key_down(key):
    global x, y
    if key == keys.DOWN:
        y = 1
    if key == keys.UP:
        y = -1
    if key == keys.LEFT:
        x = -1
    if key == keys.RIGHT:
        x = 1


pgzrun.go()
