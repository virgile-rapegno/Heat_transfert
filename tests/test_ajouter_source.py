import numpy as np
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


from src.ajouter_source import *
from src.creation_univers import *

univers_t0 = creation_univers((3, 3), 20)
T_src = 70
x_init = 1
y_init = 0


def test_ajouter_source(T_src, x_init, y_init, univers_t0):
    '''
    teste la fonction ajouter_source avec un exemple : l'univers_t0
    '''
    assert np.array_equal(ajouter_source(T_src, x_init, y_init, univers_t0), np.array(
        [[20, 70, 20], [20, 20, 20], [20, 20, 20]]))


test_ajouter_source(T_src, x_init, y_init, univers_t0)

l_src = [[70, 1, 0], [50, 2, 2]]


def test_ajouter_plusieurs_sources(l_src, univers_t0):
    '''
    teste la fonction ajouter_plusieurs_sources avec l'univers_t0
    '''
    assert np.array_equal(ajouter_plusieurs_sources(
        l_src, univers_t0), np.array([[20, 70, 20], [20, 20, 20], [20, 20, 50]]))


test_ajouter_plusieurs_sources(l_src, univers_t0)
