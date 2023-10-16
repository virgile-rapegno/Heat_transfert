import numpy as np


def creation_univers(size, T_univers):
    """
    L'univers est une matrice de cellules vides,
    donc initialisée uniquement avec une température selectionnée par l'utilisateur
    """
    return T_univers*np.ones(size)
