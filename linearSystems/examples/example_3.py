"""
    Feedback System
"""
from .example1 import serify

from ..utils.display import td

import control as ct


def feedback():
    """
        Gets the transfer function from a feedback system
    """
    # Get sys1 and sys2 transfer functions from series
    sys_g, sysh = serify(called=True)

    sys_feedback_tf = ct.feedback(sys_g, sysh, sign=1)

    td.ouput('Feedback Series TF', keys=['G(s)', 'G(c)', 'sys tf'],
             values=[sys_g, sysh, sys_feedback_tf])
