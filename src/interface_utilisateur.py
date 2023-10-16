import tkinter as tk

from src.dico_materiaux import *
from src.dico_milieu import *
from src.interface_liste import *
from src.interface_sources import *


def interface_utilisateur():
    """
    L'interface utilisateur est seullement utilisé
    pour rentrer les paramètres de l'utilisateur
    """

    root = tk.Tk()
    root.title("Simulateur de diffusion thermique")
    root.geometry("800x600")

    fenetre_parametre = tk.Frame(root)

    # Sélection de la taille
    label_taille_univers = tk.Label(
        fenetre_parametre,
        text="Taille de l'univers, x et y")
    label_taille_univers.pack()

    frame_taille_univers = tk.Frame(fenetre_parametre)

    text_taille_univers_x = tk.StringVar(frame_taille_univers)
    taille_univers_x = tk.Entry(
        frame_taille_univers,
        text=text_taille_univers_x)
    taille_univers_x.grid(row=0, column=0)

    text_taille_univers_y = tk.StringVar(frame_taille_univers)
    taille_univers_y = tk.Entry(
        frame_taille_univers,
        text=text_taille_univers_y)
    taille_univers_y.grid(row=0, column=1)

    frame_taille_univers.pack()

    # Choix de la température du materiau

    label_T_mat = tk.Label(
        fenetre_parametre,
        text="Température matériau")
    label_T_mat.pack()

    text_T_mat = tk.StringVar(fenetre_parametre)
    T_mat = tk.Entry(
        fenetre_parametre,
        text=text_T_mat)
    T_mat.pack()

    # Choix du matériau

    label_materiau = tk.Label(
        fenetre_parametre,
        text="Type de matériau")
    label_materiau.pack()

    text_materiau = tk.StringVar(fenetre_parametre)
    text_materiau.set("Type de matériau")
    opt_materiau = tk.OptionMenu(
        fenetre_parametre,
        text_materiau,
        *liste_materiau)
    opt_materiau.pack()

    # Choix du milieu

    label_milieu = tk.Label(
        fenetre_parametre,
        text="Type de milieu")
    label_milieu.pack()

    text_milieu = tk.StringVar(fenetre_parametre)
    text_milieu.set("Type de milieu")
    opt_milieu = tk.OptionMenu(
        fenetre_parametre,
        text_milieu,
        *liste_milieu)
    opt_milieu.pack()

    # Choix de la température du milieu

    label_T_amb = tk.Label(
        fenetre_parametre,
        text="Température ambiante du milieu")
    label_T_amb.pack()

    text_T_amb = tk.StringVar(fenetre_parametre)
    T_amb = tk.Entry(
        fenetre_parametre,
        text=text_T_amb)
    T_amb.pack()
    fenetre_parametre.pack()

    # Boutons pour démarrer l'affichage de la sources

    def lancer_placement(interface):
        """
        On supprime la fenetre actuelle et on charge
        la prochaine interface qu'on peut choisir
        """
        fenetre_parametre.pack_forget()
        interface(
            root,
            int(text_taille_univers_x.get()),
            int(text_taille_univers_y.get()),
            int(text_T_mat.get()),
            text_materiau.get(),
            text_milieu.get(),
            float(text_T_amb.get())
        ).pack()

    frame_boutons = tk.Frame(fenetre_parametre)
    bouton_sources_main = tk.Button(
        frame_boutons,
        text="Lancer la pose des sources à la main",
        command=lambda: lancer_placement(interface_sources))
    bouton_sources_main.pack(side=tk.LEFT)

    bouton_sources_liste = tk.Button(
        frame_boutons,
        text="Lancer la pose des sources avec une liste",
        command=lambda: lancer_placement(interface_liste))
    bouton_sources_liste.pack(side=tk.LEFT)
    frame_boutons.pack()

    fenetre_parametre.pack()
    root.mainloop()


if __name__ == "__main":
    interface_utilisateur()
