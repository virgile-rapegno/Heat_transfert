import numpy as np
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from src.evolution_cellule import *
from src.ajouter_source import *
from src.creation_univers import *


dx = 1
h = 1
lambda_0 = 1
T_amb = 20

univers_t0 = ajouter_source(50, 1, 1, creation_univers((3, 3), 20))
# on détermine univers_dt à la main (correspond à l'évolution de univers_t0 à l'instant t+dt)
univers_dt = np.array([[20, 50, 20], [50, -70, 50], [20, 50, 20]])
# on choisit des valeurs de D et dt simples pour que le calcul à la main ne soit pas trop compliqué
D1 = 1
dt1 = 1


def test_evolution_cellule(x, y):
    '''
    teste la fonction evolution_cellule pour la cellule de coordonnées x,y
    '''
    assert evolution_cellule(univers_t0, D1, h, lambda_0,
                             T_amb, x, y, dt1, dx) == univers_dt[y, x]


test_evolution_cellule(0, 2)
