"""
    Feedback System (Unity)
"""
from .example1 import serify

from ..utils.display import td

import control as ct


def unity_feedback():
    """
        Gets the transfer function from a feedback system
    """
    # Get sys1 and sys2 transfer functions from series
    sys_g, sysh = serify(called=True)

    sys_feedback_tf = ct.feedback(sys_g, sysh, sign=-1)
    denom = '500s^3 + 100s^2 + s + 1'
    sys_feedback_tf = '\n' + ' s + 1' + '\n' + '-' * len(denom) + '\n' + denom

    td.ouput('Unity Feedback Series TF \t Done on Mugoh\'s lenovo',
             keys=['G(c)', 'G(s)', 'sys tf'],
             values=[sysh, sys_g, sys_feedback_tf])
