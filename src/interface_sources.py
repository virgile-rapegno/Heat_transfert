import tkinter as tk

from src.dico_materiaux import *
from src.dico_milieu import *
from src.affichage import *
from src.creation_univers import *


def interface_sources(root, taille_x, taille_y, T_mat, materiau, milieu, T_amb):
    """
    On utilise une interface tkinter afin que l'utilisateur
    puisse rentrer exactement ses conditions initiales
    """

    # Configuration des différents conteneurs de l'interface
    fenetre_sources = tk.Frame(root)
    canvas_cellules = tk.Canvas(
        fenetre_sources,
        width=800,
        height=500
    )
    frame_cellules = tk.Frame(
        canvas_cellules,
        width=45*taille_y,
        height=30*taille_x
    )

    # Scrollbars
    h = tk.Scrollbar(canvas_cellules, orient='horizontal')
    h.pack(side=tk.BOTTOM, fill=tk.X)
    v = tk.Scrollbar(canvas_cellules)
    v.pack(side=tk.RIGHT, fill=tk.Y)

    # Variables de stockage utiles
    cellules = []
    grille = creation_univers((taille_x, taille_y), T_mat)
    sources = []

    # distinguer les conditions initiales d'une cellule (température évolue)
    # des sources dont la température reste constante
    label_source = tk.Label(
        fenetre_sources,
        text="mettre une * si le point est une source à température constante")
    label_source.pack()

    # Grille pour rentrer les conditions initiales
    for i in range(taille_x):
        ligne = []
        for j in range(taille_y):
            text_cellule = tk.StringVar(
                fenetre_sources, value=str(grille[i, j]))
            cellule = tk.Entry(
                frame_cellules,
                text=text_cellule,
                width=3)
            cellule.grid(row=i, column=j)
            ligne.append(text_cellule)
        cellules.append(ligne)

    # Mise en place des différents éléments
    canvas_cellules.create_window(0, 0, window=frame_cellules, anchor='nw')
    canvas_cellules.configure(scrollregion=canvas_cellules.bbox('all'))
    canvas_cellules.config(
        xscrollcommand=h.set,
        yscrollcommand=v.set,)
    canvas_cellules.pack()
    canvas_cellules.pack_propagate(0)
    h.config(command=canvas_cellules.xview)
    v.config(command=canvas_cellules.yview)

    def update_univers():
        """
        On récupère les conditions initiales données par
        l'utilisateur et on met à jour l'univers
        """
        nonlocal sources

        for i in range(taille_x):
            for j in range(taille_y):
                valeur_cellule = cellules[i][j].get()
                if valeur_cellule[0] == "*":  # Source fixe
                    sources.append([valeur_cellule[1:], j, i])
                    grille[i, j] = valeur_cellule[1:]
                else:  # Juste condition initiale
                    grille[i, j] = valeur_cellule

    def lancer_simulation():
        """
        On prépare l'affichage
        """
        update_univers()
        affichage(dico_materiaux[materiau], dico_milieu[milieu],
                  dico_lambda[materiau], T_amb, grille, sources)

    # Bouton pour lancer matplotlib
    bouton_simulation = tk.Button(
        fenetre_sources,
        text="Lancer simulation",
        command=lambda: [fenetre_sources.pack_forget(), lancer_simulation()])
    bouton_simulation.pack()

    return fenetre_sources
