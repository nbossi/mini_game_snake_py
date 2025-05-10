from tkinter import *
import random

# constants for game setting
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50 # how large are the food or body parts of the snake
BODY_PARTS = 3 # how many body parts at the beginning
SNAKE_COLOR = "#00FF00" # green
FOOD_COLOR = "#FF0000" # red
BACKGROUND_COLOR = "#000000" # black

# let's define all the different classes and functions that we will need
class Snake:
    pass

class Food:
    pass

def next_turn():
    pass

def change_direction():
    pass

def check_collisions():
    pass

def game_over():
    pass

# lets make our window
window = Tk()
window.title("Snake game")
window.resizable(False, False)

# Lets create a score label
score = 0
direction = 'down'

# lets create a score label
label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
#then im going to pack this label
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.mainloop()