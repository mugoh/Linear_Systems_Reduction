"""
    Zeros and Poles
"""
from terminaltables import AsciiTable

import numpy as np
import control as ct


def locate_poles():
    """
        Finds location of a system's zeros and poles
    """
    n1 = np.array([1, 1])
    n2 = np.array([1, 2])

    d1 = np.array([1, 2j])
    d2 = np.array([1, -2j])
    d3 = np.array([1, 3])

    numerator_g, denominator_g = np.array([6, 0, 1]), np.array([1, 3, 3, 1])
    sys_g = ct.tf(numerator_g, denominator_g)

    zeros_g = ct.zero(sys_g)
    pole_g = ct.pole(sys_g)

    numerator_h = np.convolve(n1, n2)
    denominator_h = np.convolve(d1, np.convolve(d2, d3))
    sys_h = ct.tf(numerator_h, denominator_h)

    sys_tf = sys_g / sys_h

    pzmap_sys = ct.pzmap(sys_tf)

    print(AsciiTable([['Poles and Zeros']]).table)
    data = [['Function', 'Result Ouput'],
            ['G(s)', sys_g],
            ['Zeros(g)', zeros_g],
            ['Pole(g)', pole_g],
            ['H(s)', sys_h],
            ['T(s)', sys_tf],
            ['Pzmap(s)', pzmap_sys]
            ]
    print(AsciiTable(data).table)
