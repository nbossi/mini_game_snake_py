# Mini Jeu Snake en Python avec Tkinter
Objectif : 
Créer un mini-jeu Snake en Python à l'aide de la bibliothèque tkinter.

## Prérequis
- Python 3 installé (idéalement via Homebrew si sur Mac)
- tkinter doit être installé (sinon, faire brew install python-tk)
- Un éditeur de code (VS Code, PyCharm, etc.)
- Terminal ou IDE pour lancer le script

## Étapes de développement
### Étape 1 – Initialiser le projet
- Créer un dossier mini_game_snake_py
- Créer un fichier main.py
- Créer un environnement virtuel si nécessaire :
```python
python3 -m venv .venv
source .venv/bin/activate
```
### Étape 2 – Créer les classes et variables nécessaires pour le jeu 
```python
# constants for game setting
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50 # how large are the food or body parts of the snake
BODY_PARTS = 3 # how many body parts at the beginning
SNAKE_COLOR = "#00FF00" # green
FOOD_COLOR = "#FF0000" # red
BACKGROUND_COLOR = "#000000" # black

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
```
### Étape 3 – Créer une fenêtre noire avec le score
- Importer les modules de base : 
```python
from tkinter import *
```
- Créer la fenêtre principale :
```python
root = Tk()
root.title("Snake Game")
```
- Définir les dimensions et créer un canevas (canvas) :
```python
canvas_width = 600
canvas_height = 400
canvas = Canvas(root, width=canvas_width, height=canvas_height, bg="black")
canvas.pack()
```
- Ajouter un label de score :
```python
score = 0
score_text = canvas.create_text(50, 10, fill="white", font="Arial 14", text=f"Score: {score}", anchor="nw")
```
- Lancer la boucle principale :
```python
root.mainloop()
```