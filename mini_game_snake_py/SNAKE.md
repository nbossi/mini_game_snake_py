# Classe Snake – Construction du serpent
## Objectif

La classe Snake représente notre serpent dans le jeu. Elle gère :
- la taille initiale du serpent,
- la position de ses parties sur la grille,
- la représentation visuelle du corps (chaque carré vert sur le canvas).

## Structure de la classe
### Constructeur __init__
‘‘‘python
class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []
‘‘‘
Explication :
- self.body_size stocke le nombre de parties du corps du serpent au début.
- self.coordinates est une liste des positions de chaque partie du corps. Chaque position est une liste [x, y].
- self.squares stocke les objets graphiques (les rectangles verts) créés dans le canvas.

### Placement initial
‘‘‘python
for i in range(0, BODY_PARTS):
    self.coordinates.append([0, 0])
‘‘‘
Au démarrage, toutes les parties du serpent sont empilées au coin supérieur gauche.
Cela crée un serpent immobile en [0,0], mais c’est volontaire : on les déplacera ensuite dans le jeu.
### Placement initial
‘‘‘python
for x, y in self.coordinates:
    square = canvas.create_rectangle(
        x, y, 
        x + SPACE_SIZE, y + SPACE_SIZE, 
        fill=SNAKE_COLOR, tag="snake"
    )
    self.squares.append(square)
‘‘‘
Détail :

- canvas.create_rectangle(...) dessine un carré vert (de taille SPACE_SIZE) pour chaque segment du serpent.
- On utilise le tag "snake" pour pouvoir facilement identifier ou supprimer ces rectangles plus tard si besoin.