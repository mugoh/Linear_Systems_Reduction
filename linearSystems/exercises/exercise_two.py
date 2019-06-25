"""
    R(s) -> Controller -> Plant -> C(s)
"""
import numpy as np
import matplotlib.pyplot as plt

from ..utils.display import td
from ..utils.helpers import get_sys


def ex_two():
    """
        Gets the closed loop transfer function of a closed loop
        feedback system
    """
    controller = np.array([[1, ],
                           [1, 1]
                           ])
    plant = np.array([[1, 2],
                      [1, 3]])

    controller_sys = get_sys(controller, sys_name='tf')
    plant_sys = get_sys(plant, sys_name='tf')

    sys_series = get_sys([controller_sys, plant_sys])
    feedback = get_sys([sys_series, get_sys([[1, ], [1, ]], 'tf')], 'feedback')

    td.ouput('Exercise Two',
             keys=['Controller', 'Plant', 'Series', 'Feedback'],
             values=[controller_sys, plant_sys, sys_series, feedback])

    T, y_out = get_sys(feedback, 'step_response')
    plt.plot(T, y_out)
    plt.title('Step Response (Exercise 2)')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.show()
