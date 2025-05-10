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
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

# 1st thing we do is updating our window so that it renders
window.update() 

# Then we need to find some dimensions
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# we need to see how much we're going to adjust
# the position of our window
x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.mainloop()