import numpy as np

from src.ajouter_source import *
from src.evolution_cellule import *


def evolution_univers(D, h, lambda_0, T_amb, univers, sources, dt, dx=0.1):
    '''
    Cette fonction détermine, à partir d'un univers à un instant t,
    l'évolution de cet univers à l'instant t+dt
    '''
    nouvel_univers = np.copy(univers)
    for i in range(len(univers)):
        for j in range(len(univers[0])):
            nouvel_univers[i, j] = evolution_cellule(
                univers, h, D, lambda_0, T_amb, j, i, dt, dx)  # on modifie chaque cellule de l'univers

    # la liste sources contient les sources de chaleur qui
    # restent fixes tout au long de l'expérience
    nouvel_univers = ajouter_plusieurs_sources(sources, nouvel_univers)
    return nouvel_univers
