import pgzrun
import random


TITLE = 'Flappy Bird'
WIDTH = 500
HEIGHT = 500

# load image
alien = Actor('alien')
aim = Actor('aim')


def draw():
    screen.fill('red')  # hex color
    alien.draw()
    aim.draw()


def update(dt):
    pass


def on_mouse_down(button, pos):
    pass


def on_mouse_move(pos):
    # x, y = pos
    aim.pos = pos


pgzrun.go()
