# Classe Food – Génération de la nourriture
## Objectif

La classe Food représente un objet à manger pour le serpent.
À chaque fois qu’elle est générée, la nourriture :
- apparaît à une position aléatoire sur la grille du jeu,
- augmente la taille du serpent lorsqu’il la mange,
- augmente le score du joueur.

## Structure de la classe
### Constructeur __init__
‘‘‘python
class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordonates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")
‘‘‘
## Détail étape par étape
### Choix de la position aléatoire
‘‘‘python
x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
‘‘‘
Explication :

- random.randint(0, n) permet de tirer un entier aléatoire.
- On divise la largeur et la hauteur du jeu par SPACE_SIZE pour obtenir le nombre de cases disponibles sur l’axe X et Y.
- On multiplie ensuite par SPACE_SIZE pour convertir ces coordonnées en pixels utilisables par le canvas.
Cela garantit que la nourriture apparaît parfaitement alignée sur la grille, comme les segments du serpent.
### Stockage des coordonnées
‘‘‘python
self.coordonates = [x, y]
‘‘‘
Cela permet de connaître la position de la nourriture dans le jeu, notamment pour détecter une collision avec la tête du serpent.
### Affichage dans l'interface
‘‘‘python
canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")
‘‘‘
Explication :
- Cette fonction dessine un cercle rouge (forme de la nourriture) dans le canvas.
- Le tag "food" permet de retrouver ou supprimer cet élément facilement.