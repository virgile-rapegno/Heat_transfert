import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from test_evolution_cellule import *
from src.evolution_univers import *


sources = [[50, 1, 1]]


def test_evolution_univers(D1, univers_t0, univers_dt, dt1, dx):
    '''
    teste la fonction evolution_univers
    '''
    assert np.array_equal(
        univers_dt, evolution_univers(D1, h, lambda_0, T_amb, univers_t0, sources, dt1, dx))


test_evolution_univers(D1, univers_t0, univers_dt, dt1, dx)
