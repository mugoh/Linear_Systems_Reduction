"""
    Closed-Loop Transfer Function and Pole zero map
"""

import control as ct
import numpy as np
import matplotlib.pyplot as plt

from ..utils.display import td
from ..utils.helpers import get_sys


def multi_loop():
    """
        Gives the transfer funtion of multi-loop system

        Feedback[ R(s) -> (G1 - H2) -> G2 -> feedback(G3G4, H1) , H3]-> C(s)
    """
    g1 = np.array([
        [1], [1, 10]])

    g2 = np.array([
        [1],
        [1, 1]]
    )
    g3 = np.array([
        [1, 0, 1],
        [1, 4, 4]
    ])
    g4 = np.array([
        [1, 1],
        [1, 6]
    ])

    h1 = np.array([
        [1, 1],
        [1, 2]
    ])
    h2 = np.array([[2], 1])
    h3 = np.array([[1], 1])

    sys_g1 = get_sys(g1, sys_name='tf')
    sys_g2 = get_sys(g2, 'tf')
    sys_g3 = get_sys(g3, 'tf')
    sys_g4 = get_sys(g4, 'tf')
    sysh1 = get_sys(h1, 'tf')
    sysh2 = get_sys(h2, 'tf')
    sysh3 = get_sys(h3, 'tf')

    td.ouput(title='Exercise One',
             keys=['G1', 'G2', 'G3', 'G4', 'H1', 'H2', 'H3'],
             values=[sys_g1, sys_g2, sys_g3, sys_g4, sysh1, sysh2, sysh3])
    sys_t = ct.series(sys_g1 - sysh2, sys_g2)
    sys_t = ct.series(sys_t,
                      ct.feedback(
                          ct.series(sys_g3, sys_g4), sysh1, sign=1))
    tS = ct.feedback(sys_t, sysh3)
    zeros, poles = ct.pzmap(tS, Plot=True, grid=True)

    show_plot(zeros, poles)

    # td.ouput('PzMap', keys=['PzMap'], values=[pz])


def show_plot(z, pl):
    """
        Creates a plot of zeros and poles
    """
    plt.plot(z, pl)
    plt.xlim([-15, 5])
    plt.ylim([-15, 5])
    plt.show()
