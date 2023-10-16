import numpy as np
import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from src.creation_univers import *


size = (3, 3)
T_univers = 20


def test_creation_univers(size, T_univers):
    '''
    teste la fonction creation_univers pour un univers de taille (3,3)
    '''
    assert np.array_equal(creation_univers(size, T_univers), np.array(
        [[20, 20, 20], [20, 20, 20], [20, 20, 20]]))


test_creation_univers(size, T_univers)
