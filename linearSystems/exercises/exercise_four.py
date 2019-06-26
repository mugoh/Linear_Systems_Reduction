
"""
    G(s) = s + 1/ s + 2
    H(s) = 1 / s + 1

    Importance of canceling common poles and zeros in a transfer function:

    - To cancel slow poles (poles with negative real parts,
        thus stable, but situated near to the imaginary axis).

    - Zeros should be added with the controller’s transfer function only to
        cancel stable poles (have negative real part) which are quite far from
        the imaginary axis.
"""


import numpy as np
import control as ct

from matplotlib import pyplot as plt

from ..utils.display import td
from ..utils.helpers import get_sys


def ex_four():
    """
        Cancels common poles and zeros in a system TF
    """
    g = np.array([
        [1, 1],
        [1, 2]]
    )
    h = np.array([
        [1, ],
        [1, 1]
    ])

    sys_g = get_sys(g, sys_name='tf')
    sys_h = get_sys(h, sys_name='tf')

    sys_t = ct.feedback(sys_g, sys_h)
    poles, zeros = ct.pzmap(sys_t, grid=True)

    td.ouput('Exercise Four\t\tDone on mugoh\'s Lenovo',
             keys=['G(s)', 'H(s)', 'T(s)'],
             values=[sys_g, sys_h, sys_t])
    td.ouput('Poles and Zeros',
             keys=['Poles', 'Zeros'],
             values=[poles, zeros])

    plt.plot(poles, zeros)
    print('\n')
    rsys = ct.minreal(sys_t)
    poles, zeros = ct.pzmap(rsys, grid=True)

    plt.plot(poles, zeros)
    plt.title('Pole Zero Map (Common poles & zeros Cancelled)')
    plt.legend(['a', 'b'])
    td.ouput('Poles and Zeros (Minreal)',
             keys=['Poles', 'Zeros'],
             values=[poles, zeros])

    plt.show()
