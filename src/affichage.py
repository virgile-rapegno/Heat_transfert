import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from src.ajouter_source import *
from src.dico_materiaux import *
from src.dico_milieu import *
from src.evolution_univers import *


def affichage(D, h, lambda_0, T_amb, univers, sources):
    """
    Fonction qui crée une animation en matplotlib de l'évolution de la température du matériau.
    """

    # création fenêtre matplotlib
    fig = plt.figure("Simulateur de diffusion thermique")

    # on crée la première image pour la génération 0
    univers_temp = ajouter_plusieurs_sources(sources, univers)
    im = plt.imshow(
        univers_temp,
        animated=True,
        cmap='coolwarm')

    # On cherche les extrema pour l'echelle de couleur
    Tmin = min(np.min(univers), T_amb)
    Tmax = max(np.max(univers), T_amb)

    # on affiche l'échelle de couleur
    plt.colorbar(label='Température en degré Celsius')
    plt.clim(Tmin, Tmax)

    # Mémorisation du temps lors du phénomène physique
    temps = 0

    def animate():
        """
        Fonction à répéter pour l'animation
        """
        nonlocal univers_temp
        nonlocal temps
        # Nous avons convenu de travailler par pas de temps de dt=1s et dx=dy=0,1m
        # Ces valeurs ont été décidées en testant la simulation avec plusieurs valeurs
        # et également pour avoir des données physiques réalistes
        temps += 1
        univers_temp = evolution_univers(
            D, h, lambda_0, T_amb, univers_temp, sources, dt=1, dx=0.1)
        im.set_array(univers_temp)
        plt.title('temps='+str(time.strftime('%Hh %Mm %Ss', time.gmtime(temps))))
        return im

    ani = animation.FuncAnimation(fig, lambda _: animate(), interval=100)

    plt.show()
