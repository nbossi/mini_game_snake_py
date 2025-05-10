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
### Étape 3 – Création de la fenêtre de jeu Snake
#### Importer les modules de base : 
```python
from tkinter import *
```
#### Créer la fenêtre principale :
```python
root = Tk()
root.title("Snake Game")
```
#### Définir les dimensions et créer un canevas (canvas) :
```python
canvas_width = 600
canvas_height = 400
canvas = Canvas(root, width=canvas_width, height=canvas_height, bg="black")
canvas.pack()
```
#### Ajout du score avec un label
```python
label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()
```
On crée un Label (étiquette) affichant le score du joueur.
La police utilisée est Consolas en taille 40 pour bien voir le texte.
pack() ajoute le label en haut de la fenêtre automatiquement.
####  Création de la zone de jeu avec un Canvas
```python
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()
```
Canvas est la surface sur laquelle le jeu va être dessiné.
La couleur de fond (bg) est définie par la variable BACKGROUND_COLOR.
Les dimensions sont fixées avec GAME_HEIGHT et GAME_WIDTH.
#### Mise à jour immédiate de la fenêtre
```python
window.update()
```
Force une première mise à jour de l'interface pour que toutes les dimensions soient calculables juste après.
####  Récupération des dimensions écran/fenêtre
```python
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
```
Ces lignes permettent de connaître la taille réelle de la fenêtre, et la taille de l'écran.
####  Centrage de la fenêtre sur l'écran
```python
x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")
```
- Calcule la position x et y pour centrer la fenêtre sur l'écran principal.
- Applique cette position avec geometry() pour un affichage plus professionnel.
#### Lancement de la boucle principale
```python
window.mainloop()
```
Démarre la boucle d'événements Tkinter pour que la fenêtre reste ouverte et réactive.

## Etape : Création de la classe Food
Objectifs de cette étape :
- Générer de la nourriture à une position aléatoire sur la grille.
- Dessiner un petit cercle coloré représentant la nourriture.
### Implémentation de la classe Food
```python
class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordonates = [x, y]
        
        canvas.create_oval(
            x, y, 
            x + SPACE_SIZE, y + SPACE_SIZE, 
            fill=FOOD_COLOR, tag="food"
        )
```
- La nourriture est placée sur la grille, donc x et y sont des multiples de SPACE_SIZE (la taille d’une cellule).
- On utilise random.randint() pour choisir une position entre 0 et nb_cases - 1.
- create_oval(...) dessine un cercle sur le canvas, représentant la nourriture.
### Résultat attendu à ce stade 
Un petit cercle de couleur FOOD_COLOR apparaît aléatoirement sur la grille à chaque création d’objet Food.