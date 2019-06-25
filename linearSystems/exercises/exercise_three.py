"""
    Step response at 10 degrees input
"""

from ..utils.helpers import get_sys
from ..utils.display import td

import numpy as np
import control as ct
from matplotlib import pyplot as plt


def ex_three():
    """
        Computes given single axis control system

        Unity Feedback R(s) -> controller -> spacecraft -> C(s)
    """
    J = k = 10.8e8
    a = 1
    b = 8

    angle = 10 * 22 / 7 * 1 / 180
    controller = np.array((
        [k, k * a],
        [1, b])
    )
    space_craft = np.array([
        [1, ],
        [J, 0, 0]
    ])

    controller_sys = get_sys(controller, sys_name='tf')
    space_craft_sys = get_sys(space_craft, sys_name='tf')

    sys_series = get_sys((controller_sys, space_craft_sys))
    feedback = get_sys([sys_series, get_sys(
                        np.array([
                            [1, ],
                            [1, ]
                        ]), 'tf')], 'feedback')

    td.ouput('Exercise Three',
             keys=['Controller', 'Space-craft', 'Feedback'],
             values=[controller_sys, space_craft_sys, feedback])

    sys_angle = feedback * angle
    t = np.arange(100.0, step=.1)
    y = ct.step_response(sys_angle, t)

    J *= .8
    controller[1] *= J
    space_craft[1] *= J

    controller_sys = get_sys(controller, 'tf')
    space_craft_sys = get_sys(space_craft, 'tf')

    feedback_ = ct.feedback(controller_sys, space_craft_sys)
    sys_angle = feedback_ * angle
    y1 = ct.step_response(sys_angle, t)

    J *= .5
    controller[1] *= J
    space_craft[1] *= J

    controller_sys = get_sys(controller, 'tf')
    space_craft_sys = get_sys(space_craft, 'tf')

    feedback_ = ct.feedback(controller_sys, space_craft_sys)
    sys_angle = feedback_ * angle
    y2 = ct.step_response(sys_angle, t, grid=True)

    plt.plot(t, y * 180 * 7 / 22)
    plt.plot(t, y1 * 180 * 7 / 22)
    plt.plot(t, y2 * 180 * 7 / 22)
    plt.xlabel('Time (sec)')
    plt.ylabel('Spacecraft Altitude')
    plt.title('Response to 10 deg step attitude change')

    plt.show()
