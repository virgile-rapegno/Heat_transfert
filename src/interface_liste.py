import tkinter as tk

from src.creation_univers import *
from src.dico_materiaux import *
from src.dico_milieu import *
from src.affichage import *
from src.ajouter_source import *


def interface_liste(root, taille_x, taille_y, T_mat, materiau, milieu, T_amb):
    """
    On utilise une interface tkinter pour rentrer
    les sources fixes à l'aide d'une liste
    """

    # Structure graphique
    fenetre_liste = tk.Frame(root)

    label_liste = tk.Label(
        fenetre_liste,
        text="""
            Entrer une liste de la forme T1,x1,y1;T2,x2,y2;...
            on utilise ; pour separer les tuples
            """)
    label_liste.pack()

    text_entree_liste = tk.StringVar(fenetre_liste)
    entree_liste = tk.Entry(
        fenetre_liste,
        text=text_entree_liste)
    entree_liste.pack()

    def stringvar_en_liste(liste):
        """
        On convertit l'entrée de l'utilisateur
        en liste de liste
        donc T1,x1,y1;T2,x2,Y2 -> [[T1,x1,y1],[T2,x2,Y2]]
        """
        res = []
        nouvelle_liste = liste.get().split(";")
        for sous_liste in nouvelle_liste:
            res.append(list(map(int, sous_liste.split(","))))
        return res

    def lancer_simulation():
        """
        On crée l'univers avec les sources données par l'utilisateur
        puis on lance l'affichage
        """
        nonlocal text_entree_liste

        liste_sources = stringvar_en_liste(text_entree_liste)

        univers = ajouter_plusieurs_sources(
            liste_sources,
            creation_univers(
                (taille_x, taille_y),
                T_mat))

        affichage(
            dico_materiaux[materiau],
            dico_milieu[milieu],
            dico_lambda[materiau],
            T_amb,
            univers,
            liste_sources)

    # Bouton pour lancer la simulation
    bouton_simulation = tk.Button(
        fenetre_liste,
        text="Lancer simulation",
        command=lambda: [fenetre_liste.pack_forget(), lancer_simulation()])
    bouton_simulation.pack()

    return fenetre_liste
